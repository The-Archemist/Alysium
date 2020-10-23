import re
from commands.command import Command
from django.conf import settings
from evennia import CmdSet
from evennia.utils import evtable, utils
from evennia.utils.ansi import strip_ansi

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
        self.add(CmdGive())
        self.add(CmdInventory())
        self.add(CmdLook())
        self.add(CmdSay())

class CmdDrop(Command):
    """
    Command:
      drop all                    Drop everything from your inventory.
      drop <object>               Drop an item from your inventory.

    Usage:
      Drop objects from your inventory into the room.
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

        if not target and not len(caller.contents) > 0:
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
    Command:      
      get all                Gets everything from the room.
      get <object>           Gets an object from the room.

    Usage:
      Get objects from the room and move them into your inventory.
    """

    key = "get"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """implements the command."""

        caller = self.caller
        target = self.args.strip()

        if not target:
            caller.msg("Get what?")
            return

        if target == "all":
            for obj in caller.location.contents:
                if not obj.at_before_get(caller):
                    continue

                if obj == caller:
                    continue

                self.get(obj)
            return

        obj = caller.search(target, location=caller.location)
        if not obj:
            return

        if caller == obj:
            caller.msg("You cannot get yourself.")
            return

        if not obj.access(caller, "get"):
            if obj.db.get_err_msg:
                caller.msg(obj.db.get_err_msg)
            else:
                caller.msg(f"You cannot get {obj.name}.")
            return

        # calling at_before_get hook method
        if not obj.at_before_get(caller):
            return

        self.get(obj)

    def get(self, obj):
        caller = self.caller
        success = obj.move_to(caller, quiet=True)

        if not success:
            caller.msg(f"You cannot get {obj.name}.")
        else:
            caller.msg(f"You get {obj.name}.")
            caller.location.msg_contents(f"{caller.name} gets {obj.name}.", exclude=caller)
            
            #call at_get hook
            obj.at_get(caller)

class CmdGive(Command):
    """
    Command:
      give <object> to <target>

    Usage:
      Give objects from your inventory to others.
    """
    
    key = "give"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def parse(self):
        self.args = self.args.strip()
        self.quantity = None
        self.object = None
        self.target = None

        #match.group(1) = quantity
        #match.group(2) = object
        #match.group(3) = target
        match = re.search(r"^(\d+)?\s?(\S+) to (\S+)$", self.args)
        if match is not None:
            #self.quantity = match.group(1)
            self.object   = match.group(2)
            self.target   = match.group(3)

    def func(self):
        """Implement the command"""
        caller = self.caller
        #quantity = self.quantity
        obj    = self.object
        target = self.target

        if not self.args or not obj or not target:
            caller.msg("Usage: give <object> to <target>.")
            return

        obj = caller.search(
            obj,
            location = caller,
            nofound_string = f"You are not carrying {obj}.",
            multimatch_string = f"You are carrying more than one {obj}:"
        )

        target = caller.search(target)
        if not (obj and target):
            return
        
        if target == caller:
            caller.msg(f"You keep {obj.key} to yourself.")
            caller.location.msg_contents(f"{caller.name} keeps {obj.key} all to themselves.", exclude=caller)
            return

        if not obj.location == caller:
            caller.msg(f"You are not carrying {obj.key}.")
            return

        #Calling at_before_give hook
        if not obj.at_before_give(caller, target):
            return

        #Give object
        caller.msg(f"You give {obj.key} to {target.key}.")
        caller.location.msg_contents(f"{caller.name} gives {obj.key} to {target.key}.", exclude=(caller, target))
        obj.move_to(target, quiet=True)
        target.msg(f"{caller.key} gives {obj.key} to you.")

        #Call object's at_give script
        obj.at_give(caller, target)

class CmdInventory(Command):
    """
    Command:
      i
      inv
      inventory

    Usage:
      Shows your inventory.
    """

    key = "inventory"
    aliases = ["inv", "i"]
    locks = "cmd:all()"
    arg_regex = r"$"

    def func(self):
        """Implement give command"""

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
    Command:
      look
      look <obj>

    Usage:
      Observes your location or objects in your vicinity.
    """

    key = "look"
    aliases = ["l"]
    locks = "cmd:all()"
    help_category = "Character Commands"
    
    def func(self):
        """Implement look command"""

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

class CmdSay(Command):
    """
    Command:
      say <message>

    Usage:
      Talk to those in your current location.
    """

    key = "say"
    aliases = ["'"]
    locks = "cmd:all()"

    def parse(self):
        self.args = self.args.strip()
        self.target = None
        self.speech = None
        self.targeted = False

        #match.group(1) = to if exists
        #match.group(2) = target if to exists else message
        #match.group(3) = message
        match = re.search(r"^(to)?\s*(\S+)(.*)$", self.args)
        if match is not None:
            if match.group(1) is not None:
                target = match.group(2)
                self.target = self.caller.search(target, nofound_string="To who?")
                self.speech = match.group(3).strip()
                self.targeted = True
            else:
                self.speech = (match.group(2) + match.group(3)).strip()
                
    def func(self):
        """Impelement say command"""

        caller = self.caller
        target = self.target
        speech = self.speech
        targeted = self.targeted

        if not self.args:
            caller.msg("Say what?")

        if not caller.account.is_superuser:
            speech = strip_ansi(speech)

        #Call at_before_say
        speech = caller.at_before_say(speech)

        if not speech:
            return

        #Call at_after_say
        caller.at_say(speech, target, targeted)