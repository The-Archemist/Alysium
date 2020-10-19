import datetime
from commands.command import Command
from django.conf import settings
from evennia import CmdSet
from evennia.server.sessionhandler import SESSIONS
from evennia.utils.utils import dedent, fill

class AccountCmdSet(CmdSet):
    """
    Implements the account command set. Used for universal commands.
    """

    key = "AccountCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Account-specific commands
        self.add(CmdHelp())
        self.add(CmdPassword())
        self.add(CmdQuit())
        self.add(CmdWho())

from evennia.commands.default.help import CmdHelp as default_help
class CmdHelp(default_help):
    """
    View help or a list of topics

    Usage:
      help <topic or command>
      help list
      help all

    This will search for help on commands and other
    topics related to the game.
    """

    key = "help"
    locks = "cmd:all()"
    help_category = "Account Commands"

    def format_help_entry(self, title, help_text, aliases=None, suggested=None):
        """
        This visually formats the help entry.
        This method can be overriden to customize the way a help
        entry is displayed.
        Args:
            title (str): the title of the help entry.
            help_text (str): the text of the help entry.
            aliases (list of str or None): the list of aliases.
            suggested (list of str or None): suggested reading.
        Returns the formatted string, ready to be sent.
        """
        _DEFAULT_WIDTH = settings.CLIENT_DEFAULT_WIDTH
        _SEP = "|C" + "-" * _DEFAULT_WIDTH + "|n"

        string = _SEP + "\n"
        if title:
            string += "|CHelp for |w%s|n" % title
        if aliases:
            string += " |C(aliases: %s|C)|n" % ("|C,|n ".join("|w%s|n" % ali for ali in aliases))
        if help_text:
            string += "\n%s" % dedent(help_text.rstrip())
        if suggested:
            string += "\n\n|CSuggested:|n "
            string += "%s" % fill("|C,|n ".join("|w%s|n" % sug for sug in suggested))
        string.strip()
        string += "\n" + _SEP + "\n"
        return string + "> "

    def format_help_list(self, hdict_cmds, hdict_db):
        """
        Output a category-ordered list. The input are the
        pre-loaded help files for commands and database-helpfiles
        respectively.  You can override this method to return a
        custom display of the list of commands and topics.
        """
        _DEFAULT_WIDTH = settings.CLIENT_DEFAULT_WIDTH
        _SEP = "|C" + "-" * _DEFAULT_WIDTH + "|n"
        help_entries = "Help Entries"
        
        string = ""
        if hdict_cmds and any(hdict_cmds.values()):
            string += "\n" + _SEP + "\n|C"+help_entries.center(_DEFAULT_WIDTH, " ")+"|n\n" + _SEP
            for category in sorted(hdict_cmds.keys()):
                string += "\n |C%s|n:\n" % (str(category).title())
                string += "|n " + fill("|n, |n".join(sorted(hdict_cmds[category]))) + "|n\n"
        if hdict_db and any(hdict_db.values()):
            string += "\n\n" + _SEP + "\n\r  |COther help entries|n\n" + _SEP
            for category in sorted(hdict_db.keys()):
                string += "\n\r  |w%s|n:\n" % (str(category).title())
                string += (
                    "|G"
                    + fill(", ".join(sorted([str(topic) for topic in hdict_db[category]])))
                    + "|n"
                )
        return string + "\n> "

    def func(self):
        super().func()

class CmdPassword(Command):
    """
    Change your password.
    
    Usage:
     password
    """

    key = "password"
    locks = "cmd:pperm(Player)"
    help_category = "Account Commands"
    account_caller = True

    def func(self):
        #Grab old password
        account = self.account
        old_pass = yield("Enter your password: ")

        #verify old pass
        if not account.check_password(old_pass):
            self.msg("Password incorrect.")
            return

        #Grab & validate new password
        new_pass = yield("Enter your new password: ")
        validated, error = account.validate_password(new_pass)

        #Send errors or set new password
        if not validated:
            for x in error.messages:
                self.msg(x)
        else:
            account.set_password(new_pass)
            account.save()
            self.msg("Password set.\n> ")
            account._send_to_info_channel(f"|R{account.name} changed passwords|n")           
            logger.log_sec(
                "Password Changed: %s (Caller: %s, IP: %s)." % (account, account, self.session.address)
            )
            return

class CmdQuit(Command):
    """
    Quit the game.

    Usage:
     quit
    """

    key = "quit"
    locks = "cmd:all()"
    help_category = "Account Commands"
    account_caller = True

    def func(self):
        account = self.account
        reason = "Quitting..."
        account.msg("You close your eyes and fall into a deep slumber.", session = self.session)
        account.disconnect_session_from_account(self.session, reason)
        return

class CmdWho(Command):
    """
    List who is currently online

    Usage:
      who

    Shows who is currently online and additional information for privileged characters.
    """

    key = "who"
    locks = "cmd:all()"
    help_category = "Character Commands"
    account_caller = True

    def func(self):
        """
        Get all connected accounts by polling sessions
        """
        account = self.account
        session_list = SESSIONS.get_sessions()
        session_list = sorted(session_list, key = lambda o: o.account.key)
        naccounts = SESSIONS.account_count()
        chars_dict = {}

        time = datetime.datetime.now()
        year = str(int(time.strftime("%Y")) - 1000)
        dmdy = time.strftime("%A, %B %d, ") + year
        dmdy = dmdy.center(55, " ")
        hm = time.strftime("%H:%M")
        hm = hm.center(57, " ")

        string =  (f"|n -------------------     |044Alysium     |n-------------------|n\n\n")
        string += (f"|n{dmdy}\n")
        string += (f"|n{hm}\n\n")
        string += (f"|n -------------------      |500Staff      |n-------------------|n\n\n")
        string += (f"|n   Jake - |500Administrator|n\n\n")
        string += (f"|n ----------------------- |220Players|n -----------------------")
        self.msg(string)

        for session in session_list:
            if not session.logged_in:
                continue

            account = session.get_account()
            if account.is_superuser:
                continue

            puppet = session.get_puppet()
            location = puppet.location.key if puppet and puppet.location else "None"
            chars_dict[account.name] = {'location' : None}
            chars_dict[account.name]['location'] = location

        for char in sorted(chars_dict.keys()):
            if self.account.check_permstring("Developer" or "Admins"):
                self.msg(f"|W   {char} ({chars_dict[char]['location']})")
            else:
                self.msg(f"|W   {char}")

        count = len(chars_dict)
        if count > 1:
            string = "There are {} people in Alysium.".format(count)
        elif count == 1:
            string = "There is {} person in Alysium.".format(count)
        else:
            string = "Nobody is online."

        string = string.rjust(56, " ")
        self.msg("\n"+string)
        return
