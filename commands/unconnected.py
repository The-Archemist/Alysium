from commands.command import Command

from django.conf import settings
from evennia import CmdSet
from evennia import Command as BaseCommand
from evennia.commands.cmdhandler import CMD_LOGINSTART
from evennia.utils.ansi import strip_ansi
from evennia.utils.evmenu import EvMenu
from evennia.utils.utils import callables_from_module, class_from_module, random_string_from_module

_ACCOUNT = class_from_module(settings.BASE_ACCOUNT_TYPECLASS)
_CONNECTION_SCREEN_MODULE = settings.CONNECTION_SCREEN_MODULE
_LOGIN_MENU = "commands.unconnected"

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
            _LOGIN_MENU,
            startnode="login_username",
            auto_look=False,
            auto_quit=False,
            cmd_on_exit=None,
            node_formatter=self._node_formatter
        )

    @staticmethod
    def _node_formatter(nodetext, optionstext, caller=None):
        """Do not display the options, only the text."""
        return nodetext + "\n> "

def login_username(caller, raw_text, **kwargs):
    """
    Start the login process.

    Prompt for character name.
    """

    def _check_input(caller, username, **kwargs):
        """
        Goto callable for _default. Checks username to determine existing or
        new character.

        Return from this function will determine proceeding node.
        """
        #recreate string without color/speciaLs, then capitalize.
        username = ''.join(e for e in strip_ansi(username) if e.isalpha()).capitalize()

        if len(username) < 3:
            caller.msg("Character name must be at least three characters long.")
            return "login_username"

        try:
            _ACCOUNT.objects.get(username__iexact=username)
        except _ACCOUNT.DoesNotExist:
            # Create new character
            return "create_username", {"username" : username}
        else:
            # Login existing character
            return "login_password", {"username" : username}

    text = "\nEnter your character name:"
    options = (
        {"key" : "",            "goto" : "login_username"},
        {"key" : ("quit", "q"), "goto" : "login_quit"},
        {"key" : "_default",    "goto" : _check_input}
    )
    return text, options

def login_password(caller, raw_text, **kwargs):
    """
    Prompt for password input.
    """
    def _check_input(caller, password, **kwargs):
        """
        Goto for _default. Will determine if authentication
        succeeds and push character onward to login.
        """
        username = kwargs['username']
        password = password.rstrip("\n")
        session = caller
        address = session.address

        account, errors = _ACCOUNT.authenticate(
            username=username, password=password, ip=address, session=session
        )

        if account:
            return "login_complete", {"account" : account}
        else:
            session.msg(f"{errors}")
            return "login_username"

    username = kwargs["username"]
    text = "\nEnter password:"
    options = (
        {"key" : "",            "goto" : "login_username"},
        {"key" : ("quit", "q"), "goto" : "login_quit"},
        {"key" : "_default",    "goto" : (_check_input, kwargs)}
    )

    return text, options

def login_complete(caller, raw_text, **kwargs):
    """
    Exit menu, login.
    """
    session = caller
    account = kwargs.get("account")
    session.sessionhandler.login(session, account)

    return "", {}

def login_quit(caller, raw_text, **kwargs):
    """
    Quit menu, disconnect.
    """
    session = caller
    session.sessionhandler.disconnect(session, "Goodbye!")
    return "", {}


"""

Character Creation

"""

def create_username(caller, raw_text, **kwargs):
    """
    Prompt for character name confirmation.
    """

    def _check_input(caller, response, **kwargs):
        response = response.rstrip("\n")
        if response.upper() == "Y":
            return "create_password", {"username" : username}
        elif response.upper() == "N":
            return "login_username", {}
        else:
            return "create_username", kwargs

    username = kwargs['username']
    text = f"""
        Welcome to Alysium!

        The following rules apply to names:

        1. Modern names are not allowed. (Ex: Hailey, Saul)
        2. Mythological names are not allowed. (Ex: Zeus, Hades)
        3. Popular literature names are not allowed. (Ex: Gandalf, Frodo)
        4. Dictionary words used for names are not allowed. (Ex: Death, Life)

        Is the name {username} correct and adhere to the above rules? (Y/N)

    """
    options = (
        {"key" : "",            "goto" : "login_username"},
        {"key" : ("quit", "q"), "goto" : "login_quit"},
        {"key" : "_default",    "goto" : (_check_input, kwargs)}
    )

    return text, options

def create_password(caller, raw_text, **kwargs):
    """
    Prompt for character password confirmation.
    """

    def _check_input(caller, password, **kwargs):
        username = kwargs['username']
        password = password.rstrip("\n")
        session = caller
        address = session.address

        account, errors = _ACCOUNT.create(
            username=username, password=password, ip=address, session=session
        )

        if account:
            session.msg(f"{username} has been created. Welcome!")
            return "create_login", {"account" : account}
        else:
            #restart due to errors.
            for error in errors:
                session.msg(f"{error}")

            kwargs["retry_password"] = True
            return "create_password", kwargs

    text = "Enter a password:"
    options = (
        {"key" : "", "goto" : "login_username"},
        {"key" : ("quit", "q"), "goto" : "login_quit"},
        {"key" : "_default", "goto" : (_check_input, kwargs)}
    )

    return text, options

def create_login(caller, raw_text, **kwargs):
    """
    Exit creation, login.
    """
    session = caller
    account = kwargs.get("account")
    session.sessionhandler.login(session, account)

    return "", {}