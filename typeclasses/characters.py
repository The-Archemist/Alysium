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
from server.utils.wrap import wrap


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

    #def at_before_get(self, getter, **kwargs):
    #    getter.msg("You cannot get %s." % self)
    #    return False

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
        #Capitalize the speech and strip final space

        #Ensure speech ends appropriately.
        if not speech.endswith((".", "!", "?", ".'", '."', "!'", '!"', "?'", '?"')):
            speech = speech + "."

        prefixes = {
            #Target Prefixes - All
            "all" : {
                #Inflection Prefixes - Say
                "say" : {     
                    #Message Type       
                    "self" : {
                        #Volume Prefixes
                        "normal" : f'You say, "',
                        "loud"   : f'You loudly say, "',
                        "quiet"  : f'You quietly say, "'
                    },

                    #Message Type 
                    "room" : {
                        #Volume Prefixes
                        "normal" : f'{self} says, "',
                        "loud"   : f'{self} loudly says, "',
                        "quiet"  : f'{self} quietly says, "'
                    }
                },

                #Inflection Prefixes - Say
                "exclaim" : {
                    #Message Type 
                    "self" : {
                        #Volume Prefixes
                        "normal" : f'You exclaim, "',
                        "loud"   : f'You loudly exclaim, "',
                        "quiet"  : f'You quietly claim, "'
                    },

                    #Message Type 
                    "room" : {
                        #Volume Prefixes
                        "normal" : f'{self} exclaims, "',
                        "loud"   : f'{self} loudly exclaims, "',
                        "quiet"  : f'{self} quietly exclaims, "'
                    }
                },
                
                #Inflection Prefixes - Say
                "ask" : {
                    #Message Type 
                    "self" : {
                        #Volume Prefixes
                        "normal" : f'You ask, "',
                        "loud"   : f'You loudly ask, "',
                        "quiet"  : f'You quietly ask, "'
                    },

                    #Message Type 
                    "room" : {
                        #Volume Prefixes
                        "normal" : f'{self} asks, "',
                        "loud"   : f'{self} loudly asks, "',
                        "quiet"  : f'{self} quietly asks, "'
                    }
                }
            },

            #Target Prefixes - Targeted
            "target" : {
                #Inflection Prefixes - Say
                "say" : {      
                    #Message Type       
                    "self" : {
                        #Volume Prefixes
                        "normal" : f'You say to {target}, "',
                        "loud"   : f'You loudly says to {target}, "',
                        "quiet"  : f'You quietly says to {target}, "'
                    },
                    
                    #Message Type 
                    "room" : {
                        #Volume Prefixes
                        "normal" : f'{self} says to {target}, "',
                        "loud"   : f'{self} loudly says to {target}, "',
                        "quiet"  : f'{self} quietly says to {target}, "'
                    },

                    #Message Type 
                    "target" : {
                        #Volume Prefixes
                        "normal" : f'{self} says to you, "',
                        "loud"   : f'{self} loudly says to you, "',
                        "quiet"  : f'{self} quietly says to you, "'
                    }
                },

                #Inflection Prefixes - Exclaim
                "exclaim" : {
                    #Message Type 
                    "self" : {
                        #Volume Prefixes
                        "normal" : f'You exclaim to {target}, "',
                        "loud"   : f'You loudly exclaim to {target}, "',
                        "quiet"  : f'You quietly claim to {target}, "'
                    },

                    #Message Type 
                    "room" : {
                        #Volume Prefixes
                        "normal" : f'{self} exclaims to {target}, "',
                        "loud"   : f'{self} loudly exclaims to {target}, "',
                        "quiet"  : f'{self} quietly exclaims to {target}, "'
                    },

                    #Message Type 
                    "target" : {
                        #Volume Prefixes
                        "normal" : f'{self} exclaims to you, "',
                        "loud"   : f'{self} loudly exclaims to you, "',
                        "quiet"  : f'{self} quietly exclaims to you, "'
                    }
                },

                #Inflection Prefixes - Ask
                "ask" : {
                    #Message Type 
                    "self" : {
                        #Volume Prefixes
                        "normal" : f'You ask {target}, "',
                        "loud"   : f'You loudly ask {target}, "',
                        "quiet"  : f'You quietly ask {target}, "'
                    },

                    #Message Type 
                    "room" : {
                        #Volume Prefixes
                        "normal" : f'{self} asks {target}, "',
                        "loud"   : f'{self} loudly asks {target}, "',
                        "quiet"  : f'{self} quietly asks {target}, "'
                    },

                    #Message Type 
                    "target" : {
                        #Volume Prefixes
                        "normal" : f'{self} asks you, "',
                        "loud"   : f'{self} loudly asks you, "',
                        "quiet"  : f'{self} quietly asks you, "'
                    }
                }               
            }
        }

        if not target:
            target_prefix = "all"
        else:
            target_prefix = "target"

        if speech.endswith(("!", "!'", '!"')):
            inflection_prefix = "exclaim"
        elif speech.endswith(("?", "?'", '?"')):
            inflection_prefix = "ask"
        else:
            inflection_prefix = "say"

        if volume in ("lsay", '"'):
            volume_prefix = "loud"
        elif volume == "qsay":
            volume_prefix = "quiet"
        else:
            volume_prefix = "normal"

        self_text = prefixes[target_prefix][inflection_prefix]["self"][volume_prefix]
        room_text = prefixes[target_prefix][inflection_prefix]["room"][volume_prefix]

        self_speech = wrap(speech, pre_text = self_text) + '"'
        room_speech = wrap(speech, pre_text = room_text) + '"'
        self.msg(self_speech)
        self.location.msg_contents(room_speech, exclude = (self, target))
        if target:
            target_text = prefixes[target_prefix][inflection_prefix]["target"][volume_prefix]
            target_speech = wrap(speech, pre_text = target_text) + '"'
            target.msg(target_speech)


    pass
