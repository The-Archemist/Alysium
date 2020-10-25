import re
from commands.command import Command
from evennia import CmdSet
from server.utils.utils import grammarize, wrap

class SocialCmdSet(CmdSet):
    """
    Implements the social command set.
    """

    key = "SocialCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Social-specific commands
        self.add(CmdAck())

class CmdAck(Command):
    """
    Command:
      ack

    Example: You ack.
    """

    key = "ack"
    locks = "cmd:all()"
    auto_help = False

    def parse(self):
        self.target = None
        self.extra = None

        #match.group(1) = target
        #match.group(2) = speech
        match = re.search(r"^\s*(\S+)(.*)$", self.args.strip())
        if match is not None:
            self.target = self.caller.search(match.group(1))
            if self.target:
                self.extra = match.group(2).strip()
            else:
                self.extra = (match.group(1) + match.group(2)).strip()

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You ack "
        room_msg = f"{caller.name} acks "
        target_msg = f"{caller.name} acks "

        if target:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        if extra:
            self_msg += extra
            room_msg += extra
            target_msg += extra

        caller.at_social(self_msg, room_msg, target_msg, target)

        