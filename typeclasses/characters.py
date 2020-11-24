"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
import re
from evennia import DefaultCharacter
from evennia.utils.ansi import strip_ansi
from server.utils.utils import grammarize, wrap


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def at_post_unpuppet(self, account, session=None, **kwargs):
        """
        We stove away the character when the account goes ooc/logs off,
        otherwise the character object will remain in the room also
        after the account logged off ("headless", so to say).

        Args:
            account (Account): The account object that just disconnected
                from this object.
            session (Session): Session controlling the connection that
                just disconnected.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        """
        if not self.sessions.count():
            # only remove this char from grid if no sessions control it anymore.
            if self.location:

                def message(obj, from_obj):
                    obj.msg("%s closes their eyes and falls into a deep slumber." % self.get_display_name(obj), from_obj=from_obj)

                self.location.for_contents(message, exclude=[self], from_obj=self)
                self.db.prelogout_location = self.location
                self.location = None

    def at_say(self, speech, volume="say", target=None):
        speech = grammarize(speech)

        #determine volume prefix
        if volume in ("say", "'"):
            volume = ""
        elif volume in ("lsay", '"'):
            volume = "loudly "
        elif volume == "qsay":
            volume = "quietly "

        #determine inflection prefix
        if speech.endswith("."):
            self_inflection = "say"
            room_inflection = "says"
            if target:
                self_inflection += f" to {target}"
                room_inflection += f" to {target}"
                target_inflection = f"says to you"
        elif speech.endswith("!"):
            self_inflection = "exclaim"
            room_inflection = "exclaims"
            if target:
                self_inflection += f" to {target}"
                room_inflection += f" to {target}"
                target_inflection = f"exclaims to you"
        elif speech.endswith("?"):
            self_inflection = "ask"    
            room_inflection = "asks"  
            if target:
                self_inflection += f" {target}"
                room_inflection += f" {target}"
                target_inflection = f"asks you"

        #format & deliver speech
        self_msg = "You " + volume + self_inflection + ', "' 
        self_msg = wrap(speech, pre_text=self_msg) + '"'
        self.msg(self_msg)

        room_msg = f"{self} " + volume + room_inflection + ', "' 
        room_msg = wrap(speech, pre_text=room_msg) + '"'
        self.location.msg_contents(room_msg, exclude=(self,target))

        if target:
            target_msg = f"{self} " + volume + target_inflection + ', "'
            target_msg = wrap(speech, pre_text=target_msg) + '"'
            target.msg(target_msg)

    def at_social(self, self_msg, room_msg, target_msg=None, target=None, extra=None, punctuation=None):
        """
        Social arguments:

        self_msg    - message delivered to the caller.
        room_msg    - message delivered to the room.
        target_msg  - message delivered to the target if one exists.
        target      - target if one exists
        extra       - extra arguments added to augment social emote.
        punctuation - default punctuation if not otherwise supplied.

        """
        if extra:
            #see if there's multiple sentences
            if extra.startswith((".", ",", "!", "?")):
                self_msg = self_msg.strip()
                room_msg = room_msg.strip()
                target_msg = target_msg.strip()

            self_msg += extra
            room_msg += extra

            if target:
                target_msg += extra

        #add self-specified punctuation to the end
        if punctuation and (not extra or not extra.endswith((".", "!", "?"))):
            self_msg += punctuation
            room_msg += punctuation

            if target:
                target_msg += punctuation

        #wrap it to default width & send to caller
        self_msg = wrap(grammarize(self_msg))
        self.msg(self_msg)

        #wrap it to default width & send to the room, excluding caller and target
        room_msg = wrap(grammarize(room_msg))
        self.location.msg_contents(room_msg, exclude=(self,target))

        #if there is a target and it isn't caller, wrap and send
        if target and not target == self:
            target_msg = wrap(grammarize(target_msg))
            target.msg(target_msg)

    pass

