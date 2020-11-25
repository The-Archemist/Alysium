from commands.command import Command
from django.conf import settings
from evennia import CmdSet
from evennia.commands.cmdhandler import CMD_LOGINSTART
from evennia.utils import utils

CONNECTION_SCREEN_MODULE = settings.CONNECTION_SCREEN_MODULE

class UnconnectedCmdSet(CmdSet):
    """
    Implements the unconnected command set.
    """

    key = "UnconnectedCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Unconnected Commands
        self.add(CmdUnconnectedLook())

class CmdUnconnectedLook(Command):
    """
    Syntax: look

        This is the unconnected version of the look command.
        It will be called upon connection and begins the login
        process.

        All it does is display the connect screen.
    """

    key = CMD_LOGINSTART
    aliases = ["l", "look"]
    locks = "cmd:all()"

    def func(self):
        #Show connection screen

        callables = utils.callables_from_module(CONNECTION_SCREEN_MODULE)
        if "connection_screen" in callables:
            connection_screen = callables["connection_screen"]()
        else:
            connection_screen = utils.random_string_from_module(CONNECTION_SCREEN_MODULE)
            if not connection_screen:
                connection_screen = "No connection screen found. Contact an admin."

        self.caller.msg(connection_screen)

    