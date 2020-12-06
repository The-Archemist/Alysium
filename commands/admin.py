from evennia import CmdSet
from evennia.commands.default.building import CmdExamine
from commands.command import Command

class AdminCmdSet(CmdSet):
    """
    Implements the admin command set. Used for universal commands.
    """

    key = "AdminCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Account-specific commands
        self.add(CmdExamine())
        self.add(CmdHome())
        self.add(CmdQuell())

class CmdHome(Command):
    """
    Syntax: home

        Teleport to your home location.
    """

    key = "home"
    locks = "cmd:perm(Builder)"
    arg_regex = r"$"
    help_category = "Building Commands"

    def func(self):
        """Impelement the command"""
        caller = self.caller
        home = caller.home
        
        if not home:
            caller.msg("You have no home!")
        elif home == caller.location:
            caller.msg("You are already home!")
        else:
            caller.move_to(home)

class CmdQuell(Command):
    """
    Syntax: quell   - Lower your privilege status
            unquell - Raise your privilege status

        Normally the permission level of the Account is used when puppeting 
        a Character/Object to determine access. This command will switch the 
        lock system to make use of the puppeted Object's permissions instead. 
        This is useful mainly for testing.

        Hierarchical permission quelling only work downwards, thus an Account 
        cannot use a higher-permission Character to escalate their permission 
        level. Use the unquell command to revert back to normal operation.

    Note: If quelled permission is higher than Account permissions, the lowest
          of the two will be used.
    """   

    key = "quell"
    aliases = ["unquell"]
    locks = "cmd:pperm(Developer)"
    help_category = "Admin Commands"

    account_caller = True

    def _recache_locks(self, account):
        """Helper method to reset the lockhandler on an already puppeted object"""
        if self.session:
            char = self.session.puppet
            if char:
                # we are already puppeting an object. We need to reset
                # the lock caches (otherwise the superuser status change
                # won't be visible until repuppet)
                char.locks.reset()
        account.locks.reset()    

    def func(self):
        """Perform the command"""
        account = self.account
        permstr = (
            account.is_superuser
            and " (superuser)"
            or "(%s)" % (", ".join(account.permissions.all()))
        )
        if self.cmdstring in ("unquell", "unquell"):
            if not account.attributes.get("_quell"):
                self.msg("Already using normal Account permissions %s." % permstr.strip())
            else:
                account.attributes.remove("_quell")
                self.msg("Account permissions %s restored." % permstr.strip())
        else:
            if account.attributes.get("_quell"):
                self.msg("Already quelling Account %s permissions." % permstr.strip())
                return
            account.attributes.add("_quell", True)
            puppet = self.session.puppet
            if puppet:
                cpermstr = "(%s)" % ", ".join(puppet.permissions.all())
                cpermstr =  "Quelling to current puppet's permissions %s.\n" % cpermstr
                cpermstr += "Use unquell to return to normal permission usage."
                self.msg(cpermstr)
            else:
                self.msg("Quelling Account permissions%s. Use unquell to get them back." % permstr)
        self._recache_locks(account)