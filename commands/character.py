from commands.command import Command
from evennia import CmdSet
from evennia.utils import evtable, utils
from server.utils.utils import grammarize, listarize

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
    arg_regex = r"\s|$"

    def func(self):
        """Implement command"""
        caller = self.caller
        target = self.args.strip()
        error  = False

        msg     = "You drop "
        con_msg = "%s drops " % caller.name
        err_msg = "You cannot drop "

        if not target or not len(caller.contents) > 0:
            caller.msg("Drop what?")
            return
        
        if not target == "all":
            obj = caller.search(
                target,
                location = caller,
                nofound_string="You are not carrying %s." % target,
                multimatch_string="You are carrying more than one %s:" % target,
            )

            if not obj:
                return

            if not obj.at_before_drop(caller):
                return

            success = obj.move_to(caller.location, quiet=True)
            if not success:
                err_msg += f"{grammarize(obj)}."
                caller.msg(err_msg)
                return

            msg     += f"{grammarize(obj)}."
            con_msg += f"{grammarize(obj)}."

        else:    
            error_list = []    
            item_list  = []
            for obj in caller.contents:
                if not obj:
                    continue

                if not obj.at_before_drop(caller):
                    continue

                success = obj.move_to(caller.location, quiet=True)
                if not success:
                    error = True
                    error_list.append(obj)
                    continue

                item_list.append(obj)

                #call at_drop method
                obj.at_drop(caller)

            #listarize build grammatically correct list
            msg     += listarize(item_list)
            con_msg += listarize(item_list)

        caller.msg(msg)
        caller.location.msg_contents(con_msg, exclude=caller)

        if error:
            err_msg += listarize(error_list)
            caller.msg(err_msg)


class CmdGet(Command):
    """
    pick up something

    Usage:
      get <object>

    Picks up an object from your location and puts it in
    your inventory.
    """

    key = "get"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """implements the command."""
        caller = self.caller
        target = self.args.strip()
        error  = False

        msg     = "You get "
        con_msg = "%s gets " % caller.name
        err_msg = "You cannot get "

        if not target:
            caller.msg("Get what?")
            return

        if not target == "all":
            obj = caller.search(self.args, location = caller.location)
            if not obj:
                return

            if caller == obj:
                caller.msg("You cannot get yourself.")
                return

            if not obj.access(caller, "get"):
                if obj.db.get_err_msg:
                    caller.msg(obj.db.get_err_msg)
                else:
                    caller.msg("You cannot get that.")
                return

            #calling at_before_get hook method
            if not obj.at_before_get(caller):
                return

            success = obj.move_to(caller, quiet=True)
            if not success:
                err_msg += f"{grammarize(obj)}."
                caller.msg(err_msg)
                return
            else:
                msg += f"{grammarize(obj)}."
                con_msg += f"{grammarize(obj)}."

                #calling at_get hook method
                obj.at_get(caller)

        else:
            error_list = []
            item_list  = []
            for obj in caller.location.contents:
                if not caller == obj and obj.access(caller, "get"):
                    #calling at_before_get hook method
                    if not obj.at_before_get(caller):
                        continue

                    success = obj.move_to(caller, quiet=True)
                    if not success:
                        error = True
                        error_list.append(obj)
                        continue

                    item_list.append(obj)
                    obj.at_get(caller)

            msg     += listarize(item_list)
            con_msg += listarize(item_list) 
         
        caller.msg(msg)
        caller.location.msg_contents(con_msg, exclude=caller)
        if error:
            err_msg += listarize(error_list)
            caller.msg(err_msg)

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