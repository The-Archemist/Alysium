import json, re
from commands.command import Command
from evennia import CmdSet
from server.utils.utils import grammarize, wrap

with open('commands\social.json') as socials:
    socials = json.load(socials)

class SocialCmdSet(CmdSet):
    """
    Implements the social command set.
    """

    key = "SocialCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Social-specific commands
        self.add(CmdSocial())

class CmdSocial(Command):
    """
    Standard:
    social[0] = self
    social[1] = room

    Targeted:
    social[2] = self
    social[3] = room
    social[4] = target
    """

    key = ""
    aliases = [k for k in socials]
    auto_help = False

    def parse(self):
        self.target = None
        self.extra  = None

        match = re.match(r"^\s*(\w*)\s*(.*)$", self.args)
        if match is not None:
            self.target = self.caller.search(match.group(1))
            if self.target:
                self.extra  = match.group(2)
            else:
                self.extra  = match.group(1) + " " + match.group(2)

    def func(self):
        caller = self.caller
        target = self.target
        social = self.cmdstring
        extra  = self.extra.strip() or ""

        if not target:
            self_msg = socials[social][0]
            room_msg = socials[social][1]
            msg_list = [self_msg, room_msg]
        else:
            self_msg = socials[social][2]
            room_msg = socials[social][3]
            targ_msg = socials[social][4]
            msg_list = [self_msg, room_msg, targ_msg]

        for i, msg in enumerate(msg_list):
            if not target:
                msg_list[i] = self.replace_vars(msg, caller.name, extra)
            else:
                msg_list[i] = self.replace_vars(msg, caller.name, extra, target.name)

        caller.msg(msg_list[0])
        caller.location.msg_contents(msg_list[1], exclude = (caller, target))
        if target:
            target.msg(msg_list[2])

    def replace_vars(self, text, name, extra, target=None):
        text = re.sub('%n', name, text)
        text = re.sub('%e', extra, text)
        if target:
            text = re.sub('%t', target, text)

        text = grammarize(text)
        return text
        