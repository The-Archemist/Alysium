import textwrap
from collections import defaultdict

from commands.command import Command
from server.utils.utils import wrap

from django.conf import settings
from evennia import CmdSet
from evennia.help.models import HelpEntry
from evennia.utils.utils import columnize, dedent, fill, inherits_from, string_suggestions

CMD_IGNORE_PREFIXES = settings.CMD_IGNORE_PREFIXES
HELP_MORE = settings.HELP_MORE

_DEFAULT_WIDTH = settings.CLIENT_DEFAULT_WIDTH
_FORMAT_COLOR = "|540"
_HEADER_COLOR = "|w"
_SEP = "-"
_SOCIAL_COMMAND = "commands.command.Social"

class CmdHelp(Command):
    """
    Syntax: help
            help <topic>

        View and read help documentation for commands and topics.
    """

    key = "help"
    aliases = ['?']
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    #Help messages are wrapped in EvMore, using webclient for popups.
    help_more = HELP_MORE

    def parse(self):
        """
        Input is a string containing topic to match.
        """
        self.original_args = self.args.strip()
        self.args = self.args.strip().lower()

    def func(self):
        """
        Run help entry creator.
        """
        caller = self.caller
        cmdset = self.cmdset
        query = self.args

        # suggestion cutoff ratio between 0 and 1 (1 = perfect match)
        suggestion_cutoff = 0.6
        # number of suggestions to list (0 to remove suggestions)
        suggestion_maxnum = 5

        #default to listing all help files
        if not query:
            query = "all"

        #remove duplicates created by command handler
        cmdset.make_unique(caller)

        #retrieve available commands
        all_cmds = [cmd for cmd in cmdset if self.check_show_help(cmd, caller)]
        #retrieve commands we wish to list in master list.
        #primarily used for excluding socials.
        list_cmds = [cmd for cmd in cmdset if self.should_list_cmd(cmd, caller)]
        all_topics = [topic for topic in HelpEntry.objects.all() if topic.access(caller, "view", default=True)]
        all_categories = list(
            set(
                [cmd.help_category.lower() for cmd in all_cmds] +
                [topic.help_category.lower() for topic in all_topics]
            )
        )

        #triggered if query is empty or specified to list/all.
        if query in ("list", "all"):
            #list all available help entries, grouped by category
            hdict_cmd = defaultdict(list)
            hdict_topic = defaultdict(list)

            #create dictionaries required by format_help_list.
            #filter commands that should be reached by the help system
            #but not be displayed to the table, or be displayed differently.
            for cmd in all_cmds:
                if self.should_list_cmd(cmd, caller):
                    key = (
                        cmd.auto_help_display_key
                        if hasattr(cmd, "auto_help_display_key")
                        else cmd.key
                    )
                    hdict_cmd[cmd.help_category].append(key)
            [hdict_topic[topic.help_category].append(topic.key) for topic in all_topics]

            self.msg_help(self.format_help_list(hdict_cmd, hdict_topic))
            return

        #triggered if query is for the emotelist.
        if query == "emotelist":
            emote_list = []
            for cmd in cmdset:
                if inherits_from(cmd, _SOCIAL_COMMAND):
                    emote_list.append(cmd.key)            
            emote_list.sort()

            max_len = len(max(emote_list, key=len)) + 2
            social_list = []
            for social in emote_list:
                social = social + " " * (max_len - len(social))
                social_list.append(social)

            emotelist = "\n" + wrap(" ".join(social_list))

            self.msg_help(self.format_help_entry(query, emotelist))
            return

        # build suggestion list based off vocabulary similarities.
        suggestions = None
        if suggestion_maxnum > 0:
            vocabulary = (
                [cmd.key for cmd in all_cmds if cmd] +
                [topic.key for topic in all_topics] +
                all_categories
            )
            [vocabulary.extend(cmd.aliases) for cmd in all_cmds]
            
            suggestions = [
                sugg
                for sugg in string_suggestions(
                    query, set(vocabulary), cutoff=suggestion_cutoff, maxnum=suggestion_maxnum
                )
                if sugg != query
            ]

            if not suggestions:
                suggestions = [
                    sugg for sugg in vocabulary if sugg != query and sugg.startswith(query)
                ]

        # Try to access specific command/topic
        match = [cmd for cmd in all_cmds if cmd == query]

        if not match:
            # try an iexact match with prefixes stripped from query/cmds
            _query = query[1:] if query[0] in CMD_IGNORE_PREFIXES else query

            match = [
                cmd
                for cmd in all_cmds
                for m in cmd._matchset
                if m == _query or m[0] in CMD_IGNORE_PREFIXES and m[1:] == _query
            ]

        if len(match) == 1:
            entry = match[0]
            key = entry.auto_help_display_key if hasattr(entry, "auto_help_display_key") else entry.key
            entry_format = self.format_help_entry(
                key,
                entry.get_help(caller, cmdset),
                aliases=entry.aliases,
                suggested=suggestions
            )

            self.msg_help(entry_format)
            return

        # try to match exact database entry
        match = list(HelpEntry.objects.find_topicmatch(query, exact=True))
        if len(match) == 1:
            entry_format = self.format_help_entry(
                match[0].key,
                match[0].entrytext,
                aliases=match[0].aliases.all(),
                suggested=suggestions
            )
            self.msg_help(entry_format)
            return

        # try to match categories
        if query in all_categories:
            self.msg_help(
                self.format_help_list(
                    {
                        query: [
                            cmd.auto_help_display_key
                            if hasattr(cmd, "auto_help_display_key")
                            else cmd.key
                            for cmd in all_cmds
                            if cmd.help_category == query
                        ]
                    },
                    {query: [topic.key for topic in all_topics if topic.help_category == query]},
                )
            )
            return

        # no matches found, give suggestions
        self.msg(
            self.format_help_entry(
                "", f"No help entry found for '{query}'", None, suggested=suggestions
            ),
            options={"type":"help"},
        )

            

    @staticmethod
    def check_show_help(cmd, caller):
        """
        Should the specified command appear in the help table?

        This method checks if a command should still be listed
        despite being hidden from the master list.

        Args:
          cmd    - command to be tested.
          caller - caller of help system.

        Return:
          True:  command should appear.
          False: command should not appear.

        """
        return cmd.access(caller, "view", default=True)
        

    @staticmethod
    def should_list_cmd(cmd, caller):
        """
        Checks for auto_help flag in commands to see whether or not
        it should receive a list entry.

        Args:
          cmd    - Command class from merged cmdset
          caller - Current help caller

        """
        return cmd.auto_help and cmd.access(caller)

    def msg_help(self, text):
        """
        Messages text to the caller, adding an extra oob argument to indicate
        that this is a help command result and could be rendered in a separate
        help window.
        """
        if type(self).help_more:
            usemore = True

            if self.session and self.session.protocol_key in ("websocket", "ajax/comet"):
                try:
                    options = self.account.db._saved_webclient_options
                    if options and options['helppopup']:
                        usemore = False
                except KeyError:
                    pass

            if usemore:
                evmore.msg(self.caller, text, session=self.session)
                return
        
        self.msg(text=(text, {"type" : "help"}))

    @staticmethod
    def format_help_list(hdict_cmds, hdict_db):
        """
        Output a category-ordered list. The inputs are pre-loaded help
        files for commands and database-helpfiles respectively. You can
        override this method to return a custom display of the list of
        commands and topics.
        """
        header_len = len(" [ Help System ] --")
        header_seps = "-" * (_DEFAULT_WIDTH - header_len)
        default_seps = _FORMAT_COLOR + "-" * _DEFAULT_WIDTH + "|n"

        string = f"{_FORMAT_COLOR}{header_seps} [{_HEADER_COLOR} Help System {_FORMAT_COLOR}] --|n"
        if hdict_cmds and any(hdict_cmds.values()):
            string += "\n" 
            for category in sorted(hdict_cmds.keys()):
                string += "\n " + _FORMAT_COLOR + str(category).title() + "|n:\n"
                string += "|n" + wrap("|n, ".join(sorted(hdict_cmds[category])), pre_text=" ") + "\n"

        #if hdict_db and any(hdict_db.values()):
        #    string += "\n\n" + default_seps + "\n\r  "+_HEADER_COLOR+"Other help entires|n\n" + default_seps
        #    for category in sorted(hdict_db.keys()):
        #        string += "\n\r  " + _HEADER_COLOR + str(category).title() + "|n:\n"
        #        string += "|G" + fill(", ".join(sorted([str(topic) for topic in hdict_db[category]]))) + "|n"

        return string

    @staticmethod
    def format_help_entry(query, help_text, aliases=None, suggested=None):
        """
        Visually format the help entry.

        Can be overriden to customize how an entry is displayed.

        Args:
          title (str)              - Title of the help entry.
          help_text (str)          - Text of the help entry.
          aliases (list or None)   - Alias list.
          suggested (list or None) - Suggested reading.

        Returns the formatted string, ready to be sent.
        """
        header_len = len("-- [ " + query + " ] " + "[ Help System ] --")
        header_seps = "-" * (_DEFAULT_WIDTH - header_len)

        string = f"{_FORMAT_COLOR}-- [ {_HEADER_COLOR}{query}{_FORMAT_COLOR} ] {header_seps} [ {_HEADER_COLOR}Help System {_FORMAT_COLOR}] --|n"
        if help_text:
            help_text = dedent(help_text.rstrip())
            help_text = textwrap.indent(help_text, " ")
            string += f"\n{help_text}\n"

        #if suggested:
        #    string += "\n\n Suggestions: %s" % fill(",|n ".join("%s" % sug for sug in suggested))

        #if suggested:
        #    string += f"{_FORMAT_COLOR}Suggested:|n "
        #    string += "%s" % fill(f"{_FORMAT_COLOR},|n ".join("|w%s|n" % sug for sug in suggested))

        #string = ""
        #if hdict_cmds and any(hdict_cmds.values()):
        #    string += "\n"
        return string



