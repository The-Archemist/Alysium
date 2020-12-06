import datetime
from commands.command import Command
from commands.help import CmdHelp
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
        self.add(CmdHelp()) #Native to help.py
        self.add(CmdPassword())
        self.add(CmdQuit())
        self.add(CmdWho())

class CmdPassword(Command):
    """
    Syntax: password

        Change your password.
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
    Syntax: quit

        Quit the game.
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
    Syntax: who

        Shows who is currently online and additional information.
    """

    key = "who"
    locks = "cmd:all()"
    help_category = "Account Commands"
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
