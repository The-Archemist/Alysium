import re
from commands.command import Command
from evennia import CmdSet
from evennia.utils import evtable, utils
from evennia.utils.ansi import strip_ansi
from server.utils.utils import wrap

class EmoteCmdSet(CmdSet):
    """
    Implements the emote command set. Used for universal commands.
    """

    key = "EmoteCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"

        # Account-specific commands
        self.add(CmdEmote())
        self.add(CmdOmote())
        self.add(CmdPmote())

class CmdEmote(Command):
    """
    Command:
      emote <text>
      ;<text>

    Usage:
      The standard emote conveys an action made by your character.

    Example: emote gathers you up into a hug.
    Appears: Hailey gathers you up into a hug.
    """

    key = "emote"
    aliases = [";"]
    locks = "cmd:all()"
    
    def func(self):
        """Implement emotes"""
        caller = self.caller
        emote = self.args.strip()

        if not emote:
            caller.msg("Emote what?")
            return

        if not caller.account.is_superuser:
            emote = strip_ansi(emote)
        
        if not emote.endswith((".", "!", "?", ".'", "!'", "?'", '."', '!"', '?"')):
            emote += '.'

        emote = f"->{caller} {emote}"
        emote = wrap(emote)
        caller.location.msg_contents(emote)


class CmdOmote(Command):
    """
    Command:
      omote <text> with ; representing your character

    Usage:
      The optional emote places your name somewhere within the written action.
      A semi-colon or your name are required for an omote to function.

    Example: omote Without so much as a word, ; gathers you up into a hug.
    Appears: Without so much as a word, Hailey gathers you up into a hug.

    Notes: Omotes are not possible in tells or channels. Use standard emotes
           for these modes of communication.

           Using omote to power emote another character is against the rules.
    """
      
    key = "omote"
    locks = "cmd:all()"

    def func(self):
        """Implement omotes"""
        caller = self.caller
        omote = self.args.strip()

        if not omote:
            caller.msg("Omote what?")
            return

        if not caller.account.is_superuser:
            omote = strip_ansi(omote)

        if not caller.name in omote:
            if ";" in omote:
                omote = omote.replace(';', caller.name, 1)
            else:
                caller.msg("Syntax: omote <text> with ; representing your character.")
                return

        if not omote.endswith((".", "!", "?", ".'", "!'", "?'", '."', '!"', '?"')):
            omote += '.'
        
        omote = f"->{omote}"
        omote = wrap(omote)
        caller.location.msg_contents(omote)
            
class CmdPmote(Command):
    """
    Command:
      pmote <text>

    Usage:
      The possessive emote attaches an apostrophy to your name to convey a
      possessive form.

    Example: pmote hug squeezes so hard you might pop!
    Appears: Hailey's hug squeezes so hard you might pop!
    
    Notes: pmote will start the emote with your name in a possessive fashion.
           To convey possession in the middle of an action, use omote.

           Pmotes are not possible in tells or channels. Use standard emotes
           for those modes of communication.

    """

    key = "pmote"
    locks = "cmd:all()"

    def func(self):
        """Implement pmotes"""
        caller = self.caller
        pmote = self.args.strip()

        if not pmote:
            caller.msg("Pmote what?")
            return

        if not caller.account.is_superuser:
            pmote = strip_ansi(pmote)

        if not pmote.endswith((".", "!", "?", ".'", "!'", "?'", '."', '!"', '?"')):
            pmote += '.'

        pmote = f"->{caller}'s {pmote}"
        pmote = wrap(pmote)
        caller.location.msg_contents(pmote)

        