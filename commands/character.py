from commands.command import Command
from evennia import CmdSet
from evennia.utils import evtable, utils

class CharacterCmdSet(CmdSet):
    """
    Implements the account command set. Used for universal commands.
    """

    key = "CharacterCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Account-specific commands
        self.add(CmdDrop())
        self.add(CmdGet())
        self.add(CmdInventory())
        self.add(CmdLook())

class CmdDrop(Command):
    """
    drop something

    Usage:
      drop <object>

    Drop an object from your inventory into the
    location you are currently in.
    """

    key = "drop"
    locks = "cmd:all()"

    key = "drop"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """Implement command"""

        caller = self.caller
        target = self.args.strip()

        if not target:
            caller.msg("Drop what?")
            return

        if target == "all":
            for obj in caller.contents:
                if not obj.at_before_drop(caller):
                    continue

                self.drop(obj)
            return

        # Because the DROP command by definition looks for items
        # in inventory, call the search function using location = caller
        obj = caller.search(
            target,
            location=caller,
            nofound_string="You aren't carrying %s." % target,
            multimatch_string="You carry more than one %s:" % target,
        )
        if not obj:
            return

        # Call the object script's at_before_drop() method.
        if not obj.at_before_drop(caller):
            return

        self.drop(obj)

    def drop(self, obj):
        caller = self.caller
        success = obj.move_to(caller.location, quiet=True)

        if not success:
            caller.msg(f"You cannot drop {obj.name}.")
        else:
            caller.msg(f"You drop {obj.name}.")
            caller.location.msg_contents(f"{caller.name} drops {obj.name}.", exclude=caller)
            # Call the object script's at_drop() method.
            obj.at_drop(caller)


class CmdGet(Command):
    """
    pick up something
    Usage:
      get <obj>
    Picks up an object from your location and puts it in
    your inventory.
    """

    key = "get"
    aliases = "grab"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """implements the command."""

        caller = self.caller
        target = self.args.strip()

        if not target:
            caller.msg("Get what?")
            return
        obj = caller.search(target, location=caller.location)
        if not obj:
            return
        if caller == obj:
            caller.msg("You can't get yourself.")
            return
        if not obj.access(caller, "get"):
            if obj.db.get_err_msg:
                caller.msg(obj.db.get_err_msg)
            else:
                caller.msg("You can't get that.")
            return

        # calling at_before_get hook method
        if not obj.at_before_get(caller):
            return

        success = obj.move_to(caller, quiet=True)
        if not success:
            caller.msg("This can't be picked up.")
        else:
            caller.msg("You pick up %s." % obj.name)
            caller.location.msg_contents(
                "%s picks up %s." % (caller.name, obj.name), exclude=caller
            )
            # calling at_get hook method
            obj.at_get(caller)

class CmdInventory(Command):
    """
    view inventory

    Usage:
      i
      inv
      inventory

    Shows your inventory.
    """

    key = "inventory"
    aliases = ["inv", "i"]
    locks = "cmd:all()"
    arg_regex = r"$"

    

    def func(self):
        caller = self.caller
        items = caller.contents
        if not items:
            carry_msg = "You are not carrying anything.\n"
        else:
            table = self.styled_table(border="header")
            for item in items:
                if item is items[0]:
                    table.add_row(f"{item.name}|n")
                else:
                    table.add_row(f"          {item.name}")
            carry_msg  = f"Carrying: {table}\n"
            
        _SEP = "|x" + ('-' * 30) + "|n"
        inv = "|w" + ("Inventory").center(30, " ") + "|n"
        weight = "|w" + ("Weight: 0 (2500)").center(30, " ") + "|n"
        gold = "You are not carrying any gold."
            
        header     = _SEP + "\n" + inv + "\n" + weight + "\n" + _SEP + "\n"
        closer     = gold + "\n" + _SEP
        string = header + carry_msg + closer

        caller.msg(string)

class CmdLook(Command):
    """
    look at location or object

    Usage:
      look
      look <obj>

    Observes your location or objects in your vicinity.
    """

    key = "look"
    aliases = ["l"]
    locks = "cmd:all()"
    help_category = "Character Commands"
    
    def func(self):
        caller = self.caller
        target = self.args.strip()
        location = caller.location

        if not target:
            target = location
            if not location:
                caller.msg("You have no location to look at!")
                return

        else:
            if location.db.details:
                if target in location.db.details.keys():
                    location.msg_contents(f"{caller} looks at {target}.\n", exclude = caller)
                    caller.msg(f"{location.db.details[target]}\n")
                    return
            else:
                target = caller.search(self.args.strip())
                if not target:
                    return

        caller.msg((caller.at_look(target), {"type": "look"}), options=None)