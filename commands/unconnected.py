from commands.command import Command
from server.utils.utils import wrap

from django.conf import settings
from evennia import CmdSet, create_object
from evennia import Command as BaseCommand
from evennia.commands.cmdhandler import CMD_LOGINSTART
from evennia.utils.evmenu import EvMenu
from evennia.utils.utils import callables_from_module, random_string_from_module

_CONNECTION_SCREEN_MODULE = settings.CONNECTION_SCREEN_MODULE
_LOGIN_DIALOGUE = "world.interactions.unconnected.login"

class UnconnectedCmdSet(CmdSet):
    """
    Impelements unconnected command set.
    """

    key = "UnconnectedCommands"

    def at_cmdset_creation(self):
        """
        Populate command set.
        """

        #Commands
        self.add(CmdUnconnectedLook())

class CmdUnconnectedLook(BaseCommand):
    """
    Syntax: look

        Unconnected version of the look coomand.
        Will be called upon connection and begins
        the login process.
    """

    key = CMD_LOGINSTART
    aliases = ["l", "look"]
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        #Show connection screen

        callables = callables_from_module(_CONNECTION_SCREEN_MODULE)
        if "connection_screen" in callables:
            connection_screen = callables["connection_screen"]
        else:
            connection_screen = random_string_from_module(_CONNECTION_SCREEN_MODULE)

        self.caller.msg(connection_screen)

        EvMenu(
            self.caller,
            _LOGIN_DIALOGUE,
            startnode="login_username",
            auto_look=False,
            auto_quit=False,
            cmd_on_exit=None,
            node_formatter=self._node_formatter
        )

    @staticmethod
    def _node_formatter(nodetext, optionstext, caller=None):
        """Do not display the options, only the text."""
        return nodetext + "|n\n> "

