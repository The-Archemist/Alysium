from commands.command import Command, Social
from evennia import CmdSet

class SocialCmdSet(CmdSet):
    """
    Implements the social command set.
    """

    key = "SocialCommands"

    def at_cmdset_creation(self):
        "Populates the cmdset"
        # Emotelist
        self.add(CmdEmotelist())

        # Social-specific commands
        self.add(CmdAck())
        self.add(CmdAdmire())
        self.add(CmdApologize())
        self.add(CmdApplaud())
        self.add(CmdAgree())
        self.add(CmdBeam())
        self.add(CmdBeg())
        self.add(CmdBite())
        self.add(CmdBlink())
        self.add(CmdBlush())
        self.add(CmdBoggle())
        self.add(CmdBounce())
        self.add(CmdBow())
        self.add(CmdBrb())
        self.add(CmdCackle())
        self.add(CmdCaress())
        self.add(CmdCheer())
        self.add(CmdChortle())
        self.add(CmdChuckle())
        self.add(CmdClap())
        self.add(CmdComfort())
        self.add(CmdCough())
        self.add(CmdCower())
        self.add(CmdCringe())
        self.add(CmdCross())
        self.add(CmdCry())
        self.add(CmdCurtsy())
        self.add(CmdDance())
        self.add(CmdDrool())
        self.add(CmdEek())
        self.add(CmdEep())
        self.add(CmdEye())
        self.add(CmdFacepalm())
        self.add(CmdFlex())
        self.add(CmdFlop())
        self.add(CmdFondle())
        self.add(CmdForgive())
        self.add(CmdFrench())
        self.add(CmdFrown())
        self.add(CmdGasp())
        self.add(CmdGiggle())
        self.add(CmdGlare())
        self.add(CmdGreet())
        self.add(CmdGrin())
        self.add(CmdGroan())
        self.add(CmdGrope())
        self.add(CmdGrovel())
        self.add(CmdGrowl())
        self.add(CmdGrumble())
        self.add(CmdGrunt())
        self.add(CmdHang())
        self.add(CmdHiccup())
        self.add(CmdHighfive())
        self.add(CmdHmm())
        self.add(CmdHmph())
        self.add(CmdHold())
        self.add(CmdHop())
        self.add(CmdHug())
        self.add(CmdHum())
        self.add(CmdKiss())
        self.add(CmdKneel())
        self.add(CmdLaugh())
        self.add(CmdLeer())
        self.add(CmdMoan())
        self.add(CmdMuse())
        self.add(CmdMutter())
        self.add(CmdNibble())
        self.add(CmdNod())
        self.add(CmdNudge())
        self.add(CmdNuzzle())
        self.add(CmdPace())
        self.add(CmdPanic())
        self.add(CmdPant())
        self.add(CmdPat())
        self.add(CmdPet())
        self.add(CmdPeer())
        self.add(CmdPinch())
        self.add(CmdPlead())
        self.add(CmdPoint())
        self.add(CmdPoke())
        self.add(CmdPonder())
        self.add(CmdPounce())
        self.add(CmdPout())
        self.add(CmdPuke())
        self.add(CmdPurr())
        self.add(CmdQuiver())
        self.add(CmdRoll())
        self.add(CmdRub())
        self.add(CmdRuffle())
        self.add(CmdScowl())
        self.add(CmdScratch())
        self.add(CmdScream())
        self.add(CmdShake())
        self.add(CmdShiver())
        self.add(CmdShrug())
        self.add(CmdShudder())
        self.add(CmdShuffle())
        self.add(CmdSit())
        self.add(CmdSlap())
        self.add(CmdSmack())
        self.add(CmdSmile())
        self.add(CmdSmirk())
        self.add(CmdSmooch())
        self.add(CmdSnap())
        self.add(CmdSneer())
        self.add(CmdSnicker())
        self.add(CmdSniff())
        self.add(CmdSniffle())
        self.add(CmdSnore())
        self.add(CmdSnort())
        self.add(CmdSnuggle())
        self.add(CmdSob())
        self.add(CmdSpank())
        self.add(CmdSpit())
        self.add(CmdSqueeze())
        self.add(CmdStagger())
        self.add(CmdStamp())
        self.add(CmdStand())
        self.add(CmdStare())
        self.add(CmdStifle())
        self.add(CmdStroke())
        self.add(CmdStomp())
        self.add(CmdStretch())
        self.add(CmdStrut())
        self.add(CmdStumble())
        self.add(CmdSulk())
        self.add(CmdTackle())
        self.add(CmdTap())
        self.add(CmdTease())
        self.add(CmdThank())
        self.add(CmdThink())
        self.add(CmdTickle())
        self.add(CmdTongue())
        self.add(CmdTremble())
        self.add(CmdTsk())
        self.add(CmdTwiddle())
        self.add(CmdTwirl())
        self.add(CmdTwitch())
        self.add(CmdWait())
        self.add(CmdWaltz())
        self.add(CmdWave())
        self.add(CmdWhimper())
        self.add(CmdWiggle())
        self.add(CmdWince())
        self.add(CmdWipe())
        self.add(CmdWonder())
        self.add(CmdWorship())
        self.add(CmdWow())
        self.add(CmdYawn())


class CmdEmotelist(Command):
    """
    Placeholder for help entry.
    """

    key = "emotelist"
    locks = "cmd:all()"
    help_category = "Communication"

    pass


class CmdAck(Social):
    """
    Syntax: ack

    Examples: You ack.
              You ack at Hailey.

              Hailey acks.
              Hailey acks at Saul.
              Hailey acks at you.
    """

    key = "ack"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You ack "
        room_msg = f"{caller.name} acks "
        target_msg = f"{caller.name} acks "

        if target:
            if target == caller:
                self_msg += f"at yourself "
                room_msg += f"at themselves "
            else:
                self_msg += f"at {target.name} "
                room_msg += f"at {target.name} "
                target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!") 
      
class CmdAdmire(Social):
    """
    Syntax: admire

    Examples: You stare off in admiration.
              You admire Hailey.

              Hailey stares off in admiration.
              Hailey admires Saul.
              Hailey admires you.
    """

    key = "admire"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if not target and not extra:
            self_msg = "You stare off in admiration "
            room_msg = f"{caller.name} stares off in admiration "
            caller.at_social(self_msg, room_msg)
            return

        self_msg = "You admire "
        room_msg = f"{caller.name} admires "
        target_msg = f"{caller.name} admires "

        if target:
            if target == caller:
                self_msg += f"yourself "
                room_msg += f"themselves "
            else:
                self_msg += f"{target.name} "
                room_msg += f"{target.name} "
                target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdApologize(Social):
    """
    Syntax: apologize

    Examples: You apologize.
              You apologize to Hailey.

              Hailey apologizes.
              Hailey apologizes to Saul.
              Hailey apologizes to you.
    """

    key = "apologize"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You apologize "
        room_msg = f"{caller.name} apologizes "
        target_msg = f"{caller.name} apologizes "

        if target:
            if target == caller:
                self_msg += f"to yourself "
                room_msg += f"to themself "
            else:
                self_msg += f"to {target.name} "
                room_msg += f"to {target.name} "
                target_msg += "to you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdApplaud(Social):
    """
    Syntax:applaud

    Examples: You applaud.
              You applaud Hailey.

              Hailey applauds.
              Hailey applauds Saul.
              Hailey applauds you.
    """

    key = "applaud"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You applaud "
        room_msg = f"{caller.name} applauds "
        target_msg = f"{caller.name} applauds "

        if target:
            if target == caller:
                self_msg += f"yourself "
                room_msg += f"themselves "
            else:
                self_msg += f"{target.name} "
                room_msg += f"{target.name} "
                target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!") 

class CmdAgree(Social):
    """
    Syntax: agree

    Examples: You agree.
              You agree with Hailey.

              Hailey agrees.
              Hailey agrees with Saul.
              Hailey agrees with you.
    """

    key = "agree"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You agree "
        room_msg = f"{caller.name} agrees "
        target_msg = f"{caller.name} agrees "

        if target:
            if target == caller:
                self_msg += f"with yourself "
                room_msg += f"with themselves "
            else:
                self_msg += f"with {target.name} "
                room_msg += f"with {target.name} "
                target_msg += "with you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdBeam(Social):
    """
    Syntax: beam

    Examples: You beam brightly.
              You beam at Hailey.

              Hailey beams.
              Hailey beams at Saul.
    """

    key = "beam"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You beam "
        room_msg = f"{caller.name} beams "
        target_msg = f"{caller.name} beams "

        if not target:
            if not extra or not extra[0].isalpha():
                self_msg += "brightly "
                room_msg += "brightly "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "
        else:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, ending = "!") 

class CmdBeg(Social):
    """
    Syntax: beg

    Examples: You beg.
              You beg Hailey.

              Hailey begs.
              Hailey begs Saul.
    """

    key = "beg"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You beg "
        room_msg = f"{caller.name} begs "
        target_msg = f"{caller.name} begs "

        if target:
            if target == caller:
                self_msg += f"yourself "
                room_msg += f"themselves "
            else:
                self_msg += f"{target.name} "
                room_msg += f"{target.name} "
                target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdBite(Social):
    """
    Syntax: bite

    Examples: You bite yourself.
              You bite Hailey.

              Hailey bites themself.
              Hailey bites Saul.
    """

    key = "bite"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You bite "
        room_msg = f"{caller.name} bites "
        target_msg = f"{caller.name} bites "

        if (not target or target == caller):
            if not extra or not extra[0].isalpha():
                self_msg += "yourself "
                room_msg += "themselves "
        elif target:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdBlink(Social):
    """
    Syntax: blink

    Examples: You blink.
              You blink at Hailey.

              Hailey blinks.
              Hailey blinks at Saul.
    """

    key = "blink"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You blink "
        room_msg = f"{caller.name} blinks "
        target_msg = f"{caller.name} blinks "

        if target:
            if target == caller:
                self_msg += f"at yourself "
                room_msg += f"at themselves "
            else:
                self_msg += f"at {target.name} "
                room_msg += f"at {target.name} "
                target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdBlush(Social):
    """
    Syntax: blush

    Examples: You blush a shade of pink.
              You blush at Hailey.

              Hailey blushes a shade of pink.
              Hailey blushes at Saul.
    """

    key = "blush"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You blush "
        room_msg = f"{caller.name} blushes "
        target_msg = f"{caller.name} blushes "

        if not target:
            if not extra or not extra[0].isalpha():
                self_msg += "a shade of pink "
                room_msg += "a shade of pink "
        elif target == caller:
            self_msg += f"at yourself "
            room_msg += f"at themselves "
        else:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdBoggle(Social):
    """
    Syntax: boggle

    Examples: You boggle at the concept.
              You boggle at Hailey.

              Hailey boggles at the concept.
              Hailey boggles at Saul.
    """

    key = "boggle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You boggle at "
        room_msg = f"{caller.name} boggles at "
        target_msg = f"{caller.name} boggles at "

        if not target:
            if not extra or not extra[0].isalpha():
                self_msg += "the concept "
                room_msg += "the concept "
        elif target == caller:
            self_msg += f"yourself "
            room_msg += f"themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdBounce(Social):
    """
    Syntax: bounce

    Examples: You bounce around!
              You bounce around Hailey!

              Hailey bounces around!
              Hailey bounces around Saul!
    """

    key = "bounce"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You bounce "
        room_msg = f"{caller.name} bounces "
        target_msg = f"{caller.name} bounces "

        if not target:
            if not extra or not extra[0].isalpha():
                self_msg += "around "
                room_msg += "around "
        elif target == caller:
            self_msg += "around "
            room_msg += "around "
        else:
            self_msg += f"around {target.name} "
            room_msg += f"around {target.name} "
            target_msg += "around you "          

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!") 

class CmdBow(Social):
    """
    Syntax: bow

    Examples: You bow.
              You bows to Hailey.

              Hailey bows.
              Hailey bows to Saul.
              Hailey bows to you.
    """

    key = "bow"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You bow "
        room_msg = f"{caller.name} bows "
        target_msg = f"{caller.name} bows "

        if target and not target == caller:
            self_msg += f"to {target.name} "
            room_msg += f"to {target.name} "
            target_msg += "to you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 
   
class CmdBrb(Social):
    """
    Syntax: brb

    Examples: You say, "I'll be right back."
              Hailey says, "I'll be right back."
    """

    key = "brb"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        speech = "I'll be right back."
        caller.at_say(speech)

class CmdBurp(Social):
    """
    Syntax: burp

    Examples: You burp.
              You burp at Hailey.

              Hailey burps.
              Hailey burps at Saul.
    """

    key = "burp"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You burp "
        room_msg = f"{caller.name} burps "
        target_msg = f"{caller.name} burps "

        if target:
            if target == caller:
                self_msg += f"your own name "
                room_msg += f"their own name "
            else:
                self_msg += f"in {target.name}'s face "
                room_msg += f"in {target.name}'s face "
                target_msg += "in your face "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCackle(Social):
    """
    Syntax: cackle

    Examples: You cackle with glee!
              You cackle at Hailey!

              Hailey cackles with glee!
              Hailey cackles at Saul!
              Hailey cackles at you!
    """

    key = "cackle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cackle "
        room_msg = f"{caller.name} cackles "
        target_msg = f"{caller.name} cackles "

        if not target:
            if not extra or not extra[0].isalpha():
                self_msg += "with glee "
                room_msg += "with glee "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "
        else:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!") 
  
class CmdCaress(Social):
    """
    Syntax: caress

    Examples: You caress yourself lovingly.
              You caress Hailey lovingly.

              Hailey caresses themselves lovingly.
              Hailey caresses Saul lovingly.
    """

    key = "caress"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You caress "
        room_msg = f"{caller.name} caresses "
        target_msg = f"{caller.name} caresses "

        if target == caller or (not target and (not extra or not extra[0].isalpha())):
            self_msg += "yourself "
            room_msg += "themselves "
        elif target:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        if not extra or not extra[0].isalpha():
            self_msg += "lovingly "
            room_msg += "lovingly "
            target_msg += "lovingly "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCheer(Social):
    """
    Syntax: cheer

    Examples: You cheer enthusiastically!
              You cheers for Hailey!

              Hailey cheers enthusiastically!
              Hailey cheers for Saul!
              Hailey cheers for you!
    """

    key = "cheer"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cheer "
        room_msg = f"{caller.name} cheers "
        target_msg = f"{caller.name} cheers "

        if target and not target == caller:
            self_msg += f"for {target.name} "
            room_msg += f"for {target.name} "
            target_msg += "for you "
        elif target == caller:
            self_msg += "for yourself since nobody else will "
            room_msg += "for themselves since nobody else will "
            caller.at_social(self_msg, room_msg, target_msg, target, extra=None) 
            return

        if not extra or not extra[0].isalpha():
            self_msg += "enthusiastically "
            room_msg += "enthusiastically "
            target_msg += "enthusiastically "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!") 

class CmdChortle(Social):
    """
    Syntax: chortle

    Examples: You chortle gleefully!
              You chortles at Hailey!

              Hailey chortles gleefully!
              Hailey chortles at Saul!
              Hailey chortles at you!
    """

    key = "chortle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You chortle "
        room_msg = f"{caller.name} chortles "
        target_msg = f"{caller.name} chortles "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "

        if not extra or not extra[0].isalpha():
            self_msg += "gleefully "
            room_msg += "gleefully "
            target_msg += "gleefully "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!") 

class CmdChuckle(Social):
    """
    Syntax: chuckle

    Examples: You chuckle.
              You chuckle at Hailey.

              Hailey chuckles.
              Hailey chuckles at Saul.
              Hailey chuckles at you.
    """

    key = "chuckle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You chuckle "
        room_msg = f"{caller.name} chuckle "
        target_msg = f"{caller.name} chuckle "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdClap(Social):
    """
    Syntax: clap

    Examples: You clap.
              You clap for Hailey.

              Hailey claps.
              Hailey claps for Saul.
              Hailey claps for you.
    """

    key = "clap"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You clap "
        room_msg = f"{caller.name} claps "
        target_msg = f"{caller.name} claps "

        if target and not target == caller:
            self_msg += f"for {target.name} "
            room_msg += f"for {target.name} "
            target_msg += "for you "
        elif target == caller:
            self_msg += "for yourself "
            room_msg += "for themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdComfort(Social):
    """
    Syntax: comfort

    Examples: You comfort everyone.
              You seek comfort.
              You comfort Hailey.

              Hailey comforts everyone.
              Hailey seeks comfort.
              Hailey comforts Saul.
              Hailey comforts you.
    """

    key = "comfort"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You comfort "
        room_msg = f"{caller.name} comforts "
        target_msg = f"{caller.name} comforts "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif target == caller:
            self_msg = "You seek comfort "
            room_msg = f"{caller.name} seeks comfort "
            caller.at_social(self_msg, room_msg, target_msg, target, extra)
            return
        else:
            self_msg += "everyone "
            room_msg += "everyone "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCough(Social):
    """
    Syntax: cough

    Examples: You cough.
              You cough on yourself.
              You cough on Hailey.

              Hailey coughs.
              Hailey coughs on themselves.
              Hailey coughs on Saul.
              Hailey coughs on you.
    """

    key = "cough"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cough "
        room_msg = f"{caller.name} coughs "
        target_msg = f"{caller.name} coughs "

        if target and not target == caller:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "
        elif target == caller:
            self_msg += "on yourself "
            room_msg += f"on themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCower(Social):
    """
    Syntax: cower

    Examples: You cower in terror.
              You cowers away from Hailey.

              Hailey cowers in terror.
              Hailey cowers away from Saul.
              Hailey cowers away from you.
    """

    key = "cower"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cower "
        room_msg = f"{caller.name} cowers "
        target_msg = f"{caller.name} cowers "

        if target and not target == caller:
            self_msg += f"away from {target.name} "
            room_msg += f"away from {target.name} "
            target_msg += "away from you "
        elif not extra or not extra[0].isalpha():
            self_msg += "in terror "
            room_msg += "in terror "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCringe(Social):
    """
    Syntax: cringe

    Examples: You cringe.
              You cringe at yourself.
              You cringes at Hailey.

              Hailey cringes.
              Hailey cringes at themselves.
              Hailey cringes at Saul.
              Hailey cringes at you.
    """

    key = "cringe"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cringe "
        room_msg = f"{caller.name} cringes "
        target_msg = f"{caller.name} cringes "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCross(Social):
    """
    Syntax: cross

    Examples: You cross your arms.
              You cross your arms at Hailey.

              Hailey crosses their arms.
              Hailey crosses their arms at Saul.
              Hailey crosses their arms at you.
    """

    key = "cross"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cross your arms "
        room_msg = f"{caller.name} crosses their arms "
        target_msg = f"{caller.name} crosses their arms "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra) 

class CmdCry(Social):
    """
    Syntax: cry

    Examples: You cry.
              You cry on Hailey's shoulder.

              Hailey cries.
              Hailey cries on Saul's shoulder.
              Hailey cries on your shoulder.
    """

    key = "cry"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You cry "
        room_msg = f"{caller.name} cries "
        target_msg = f"{caller.name} cries "

        if target and not target == caller:
            self_msg += f"on {target.name}'s shoulder "
            room_msg += f"on {target.name}'s shoulder "
            target_msg += "on your shoulder "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdCurtsy(Social):
    """
    Syntax: curtsy

    Examples: You curtsy.
              You curtsy to Hailey.

              Hailey curtsies.
              Hailey curtsies to Saul.
              Hailey curtsies to you.
    """

    key = "curtsy"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You curtsy "
        room_msg = f"{caller.name} curtsies "
        target_msg = f"{caller.name} curtsies "

        if target and not target == caller:
            self_msg += f"to {target.name} "
            room_msg += f"to {target.name} "
            target_msg += "to you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdDance(Social):
    """
    Syntax: dance

    Examples: You dance.
              You dance by yourself.
              You dances with Hailey.

              Hailey dances.
              Hailey dances by themselves.
              Hailey dances with Saul.
              Hailey dances with you.
    """

    key = "dance"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You dance "
        room_msg = f"{caller.name} dances "
        target_msg = f"{caller.name} dance "

        if target and not target == caller:
            self_msg += f"with {target.name} "
            room_msg += f"with {target.name} "
            target_msg += "with you "
        elif target == caller:
            self_msg += "by yourself "
            room_msg += "by themselves " 

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdDrool(Social):
    """
    Syntax: drool

    Examples: You drool.
              You drool on yourself.
              You drool on Hailey.

              Hailey drools.
              Hailey drools on themselves.
              Hailey drools on Saul.
              Hailey drools on you.
    """

    key = "drool"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You drool "
        room_msg = f"{caller.name} drools "
        target_msg = f"{caller.name} drools "

        if target and not target == caller:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "
        elif target == caller:
            self_msg += "on yourself "
            room_msg += "on themselves " 

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdEek(Social):
    """
    Syntax: eek

    Examples: You eek!
              You eeks at Hailey!

              Hailey eeks!
              Hailey eeks at Saul!
              Hailey eeks at you!
    """

    key = "eek"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You eek "
        room_msg = f"{caller.name} eeks "
        target_msg = f"{caller.name} eeks "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!")

class CmdEep(Social):
    """
    Syntax: eep

    Examples: You eep!
              You eeps at Hailey!

              Hailey eeps!
              Hailey eeps at Saul!
              Hailey eeps at you!
    """

    key = "eep"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You eep "
        room_msg = f"{caller.name} eeps "
        target_msg = f"{caller.name} eeps "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!")

class CmdEye(Social):
    """
    Syntax: eye

    Examples: You eye everyone.
              You eye Hailey.

              Hailey eyes everyone.
              Hailey eyes Saul.
              Hailey eyes you.
    """

    key = "eye"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You eye "
        room_msg = f"{caller.name} eyes "
        target_msg = f"{caller.name} eyes "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        
        if not target and (not extra or not extra[0].isalpha()):
            self_msg += "everyone "
            room_msg += "everyone "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdFacepalm(Social):
    """
    Syntax: facepalm

    Examples: You place your face into your hands and let out a long sigh.
              You look at Hailey then place your face in your hands and let 
              out a long sigh.

              Hailey places their face into their hands and lets out a long 
              sigh.
              Hailey looks at Saul then places their face into their hands and
              lets out a long sigh.
              Hailey looks at you then places their face into their hands and 
              lets out a long sigh.
    """

    key = "facepalm"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if not target or target == caller:
            self_msg = "You place your face into your hands and let out a long sigh "
            room_msg = f"{caller.name} places their face into their hands and lets out a long sigh "
            target_msg = ""
        else:
            self_msg = f"You look at {target.name} then place your face into your hands "
            room_msg = f"{caller.name} looks at {target.name} then places their face into their hands "
            target_msg = f"{caller.name} looks at you then places their face into their hands "

        caller.at_social(self_msg, room_msg, target_msg, target, extra=None)

class CmdFlex(Social):
    """
    Syntax: flex

    Examples: You flex.
              You flex in a mirror.
              You flex for Hailey.

              Hailey flexes.
              Hailey flexes in a mirror.
              Hailey flexes for Saul.
              Hailey flexes for you.
    """

    key = "flex"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You flex "
        room_msg = f"{caller.name} flexes "
        target_msg = f"{caller.name} flexes "

        if target and not target == caller:
            self_msg += f"for {target.name} "
            room_msg += f"for {target.name} "
            target_msg += "for you "
        elif target == caller:
            self_msg += "in a mirror "
            room_msg += "in a mirror "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdFlop(Social):
    """
    Syntax: flop

    Examples: You flop on the ground.
              You flop on Hailey.

              Hailey flops on the ground.
              Hailey flops on Saul.
              Hailey flops on you.
    """

    key = "flop"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You flop "
        room_msg = f"{caller.name} flops "
        target_msg = f"{caller.name} flops "

        if target and not target == caller:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "

        if not target and (not extra or not extra[0].isalpha()):
            self_msg += "on the ground "
            room_msg += "on the ground "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdFondle(Social):
    """
    Syntax: fondle

    Examples: You fondle yourself.
              You fondle Hailey.

              Hailey fondles themselves.
              Hailey fondles Saul.
              Hailey fondles you.
    """

    key = "fondle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You fondle "
        room_msg = f"{caller.name} fondles "
        target_msg = f"{caller.name} fondles "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif target == caller or not target:
            self_msg += "yourself "
            room_msg += "themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdForgive(Social):
    """
    Syntax: forgive

    Examples: You forgive yourself.
              You forgive Hailey.

              Hailey forgives themselves.
              Hailey forgives Saul.
              Hailey forgives you.
    """

    key = "forgive"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You forgive "
        room_msg = f"{caller.name} forgives "
        target_msg = f"{caller.name} forgives "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif target == caller or not target:
            self_msg += "yourself "
            room_msg += "themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdFrench(Social):
    """
    Syntax: french

    Examples: You desperately search for someone to french kiss.
              You give Hailey a deep and passionate kiss; it seems to last 
              forever.

              Hailey desperately searches for someone to french kiss.
              Hailey gives Saul a deep and passionate kiss; it seems to last 
              forever.
              Hailey gives you a deep and passionate kiss; it seems to last 
              forever.
    """

    key = "french"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if not target or target == caller:
            self_msg = "You desperately search for someone to french kiss "
            room_msg = f"{caller.name} desperately searches for someone to french kiss "
            target_msg = ""
        else:
            self_msg = f"You give {target.name} a deep and passionate kiss; it seems to last forever "
            room_msg = f"{caller.name} gives {target.name} a deep and passionate kiss; it seems to last forever "
            target_msg = f"{caller.name} gives you a deep and passionate kiss; it seems to last forever "

        caller.at_social(self_msg, room_msg, target_msg, target, extra=None)

class CmdFrown(Social):
    """
    Syntax: frown

    Examples: You frown.
              You frown at Hailey.

              Hailey frowns.
              Hailey frowns at Saul.
              Hailey frowns at you.
    """

    key = "frown"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You frown "
        room_msg = f"{caller.name} frowns "
        target_msg = f"{caller.name} frowns "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGasp(Social):
    """
    Syntax: gasp

    Examples: You gasp.
              You gasp at Hailey.

              Hailey gasps.
              Hailey gasps at Saul.
              Hailey gasps at you.
    """

    key = "gasp"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You gasp "
        room_msg = f"{caller.name} gasps "
        target_msg = f"{caller.name} gasps "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGiggle(Social):
    """
    Syntax: giggle

    Examples: You giggle.
              You giggle at Hailey.

              Hailey giggles.
              Hailey giggles at Saul.
              Hailey giggles at you.
    """

    key = "giggle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You giggle "
        room_msg = f"{caller.name} giggles "
        target_msg = f"{caller.name} giggles "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGlare(Social):
    """
    Syntax: glare

    Examples: You glare.
              You glare at Hailey.

              Hailey glares.
              Hailey glares at Saul.
              Hailey glares at you.
    """

    key = "glare"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You glare "
        room_msg = f"{caller.name} glares "
        target_msg = f"{caller.name} glares "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGreet(Social):
    """
    Syntax: greet

    Examples: You greet everyone.
              You greet Hailey.

              Hailey greets everyone.
              Hailey greets Saul.
              Hailey greets you.
    """

    key = "greet"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You greet "
        room_msg = f"{caller.name} greets "
        target_msg = f"{caller.name} greets "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif not target and not extra:
            self_msg += "everyone "
            room_msg += "everyone "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGrin(Social):
    """
    Syntax: grin

    Examples: You grin.
              You grin at Hailey.

              Hailey grins.
              Hailey grins at Saul.
              Hailey grins at you.
    """

    key = "grin"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You grin "
        room_msg = f"{caller.name} grins "
        target_msg = f"{caller.name} grins "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGroan(Social):
    """
    Syntax: groan

    Examples: You groan.
              You groan at Hailey.

              Hailey groans.
              Hailey groans at Saul.
              Hailey groans at you.
    """

    key = "groan"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You groan "
        room_msg = f"{caller.name} groans "
        target_msg = f"{caller.name} groans "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGrope(Social):
    """
    Syntax: grope

    Examples: You grope at the air.
              You grope Hailey.

              Hailey gropes at the air.
              Hailey gropes Saul.
              Hailey gropes you.
    """

    key = "grope"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You grope "
        room_msg = f"{caller.name} gropes "
        target_msg = f"{caller.name} gropes "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif not target and not extra:
            self_msg += "at the air "
            room_msg += "at the air "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGrovel(Social):
    """
    Syntax: grovel

    Examples: You grovel.
              You grovel before Hailey.

              Hailey grovels.
              Hailey grovels before Saul.
              Hailey grovels before you.
    """

    key = "grovel"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You grovel "
        room_msg = f"{caller.name} grovels "
        target_msg = f"{caller.name} grovels "

        if target and not target == caller:
            self_msg += f"before {target.name} "
            room_msg += f"before {target.name} "
            target_msg += "before you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGrowl(Social):
    """
    Syntax: growl

    Examples: You growl.
              You growls at Hailey.

              Hailey growls.
              Hailey growls at Saul.
              Hailey growls at you.
    """

    key = "growl"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You growl "
        room_msg = f"{caller.name} growls "
        target_msg = f"{caller.name} growls "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGrumble(Social):
    """
    Syntax: grumble

    Examples: You grumble.
              You grumbles at Hailey.

              Hailey grumbles.
              Hailey grumbles at Saul.
              Hailey grumbles at you.
    """

    key = "grumble"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You grumble "
        room_msg = f"{caller.name} grumbles "
        target_msg = f"{caller.name} grumbles "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif target == caller:
            self_msg += "to yourself "
            room_msg += "to themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdGrunt(Social):
    """
    Syntax: grunt

    Examples: You grunt.
              You grunts at Hailey.

              Hailey grunts.
              Hailey grunts at Saul.
              Hailey grunts at you.
    """

    key = "grunt"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You grunt "
        room_msg = f"{caller.name} grunts "
        target_msg = f"{caller.name} grunts "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdHang(Social):
    """
    Syntax: hang

    Examples: You hang your head in shame.

              Hailey hangs their head in shame.
    """

    key = "hang"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hang your head in shame "
        room_msg = f"{caller.name} hangs their head in shame "
        target_msg = f"{caller.name} hangs their head in shame "

        caller.at_social(self_msg, room_msg)

class CmdHiccup(Social):
    """
    Syntax: hiccup

    Examples: You hiccup.

              Hailey hiccups.
    """

    key = "hiccup"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hiccup "
        room_msg = f"{caller.name} hiccup "
        target_msg = f"{caller.name} hiccup "

        caller.at_social(self_msg, room_msg, extra=extra)

class CmdHighfive(Social):
    """
    Syntax: highfive

    Examples: You highfive yourself.
              You highfive Hailey.

              Hailey highfives themselves.
              Hailey highfives Saul.
              Hailey highfives you.
    """

    key = "highfive"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You highfive "
        room_msg = f"{caller.name} highfives "
        target_msg = f"{caller.name} highfives "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdHmm(Social):
    """
    Syntax: hmm

    Examples: You hmm.

              Hailey hmms.
    """

    key = "hmm"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hmm "
        room_msg = f"{caller.name} hmms "

        caller.at_social(self_msg, room_msg)

class CmdHmph(Social):
    """
    Syntax: hmph

    Examples: You hmph.
              You hmph at Hailey.

              Hailey hmphs.
              Hailey hmphs at Saul.
              Hailey hmphs at you.
    """

    key = "hmph"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hmph "
        room_msg = f"{caller.name} hmphs "
        target_msg = f"{caller.name} hmphs "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdHold(Social):
    """
    Syntax: hold

    Examples: You hold yourself.
              You hold Hailey.

              Hailey holds themselves.
              Hailey holds Saul.
              Hailey holds you.
    """

    key = "hold"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hold "
        room_msg = f"{caller.name} holds "
        target_msg = f"{caller.name} holds "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif target == caller or (not target and not extra):
            self_msg += "yourself "
            room_msg += "themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdHop(Social):
    """
    Syntax: hop

    Examples: You hop up and down!
              You hop around Hailey!

              Hailey hops up and down!
              Hailey hops around Saul!
              Hailey hops around you!
    """

    key = "hop"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hop "
        room_msg = f"{caller.name} hops "
        target_msg = f"{caller.name} hops "

        if target and not target == caller:
            self_msg += f"around {target.name} "
            room_msg += f"around {target.name} "
            target_msg += "around you "
        elif not target and not extra:
            self_msg += "up and down "
            room_msg += "up and down "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation="!")

class CmdHug(Social):
    """
    Syntax: hug

    Examples: You hug yourself.
              You hug Hailey.

              Hailey hugs themselves.
              Hailey hugs Saul.
              Hailey hugs you.
    """

    key = "hug"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hug "
        room_msg = f"{caller.name} hugs "
        target_msg = f"{caller.name} hugs "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif not target and not extra:
            self_msg += "yourself "
            room_msg += "themselves "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdHum(Social):
    """
    Syntax: hum

    Examples: You hum.
              You hum to Hailey.

              Hailey hums.
              Hailey hums to Saul.
              Hailey hums to you.
    """

    key = "hum"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You hum "
        room_msg = f"{caller.name} hums "
        target_msg = f"{caller.name} hums "

        if target and not target == caller:
            self_msg += f"to {target.name} "
            room_msg += f"to {target.name} "
            target_msg += "to you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdKiss(Social):
    """
    Syntax: kiss

    Examples: You kiss Hailey.

              Hailey kisses Saul.
              Hailey kisses you.
    """

    key = "kiss"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You kiss "
        room_msg = f"{caller.name} kisses "
        target_msg = f"{caller.name} kisses "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        else:
            self_msg = "You desperately search for someone to kiss."
            room_msg = f"{caller.name} desperately searches for someone to kiss."
            caller.at_social(self_msg, room_msg)
            return

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdKneel(Social):
    """
    Syntax: kneel

    Examples: You kneel down.
              You kneel before Hailey.

              Hailey kneels down.
              Hailey kneels before Saul.
              Hailey kneels before you.
    """

    key = "kneel"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You kneel "
        room_msg = f"{caller.name} kneels "
        target_msg = f"{caller.name} kneels "

        if target and not target == caller:
            self_msg += f"before {target.name} "
            room_msg += f"before {target.name} "
            target_msg += "before you "
        elif not target and not extra:
            self_msg += "down "
            room_msg += "down "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdLaugh(Social):
    """
    Syntax:  laugh
    Aliases: lmao
             lol
             rofl
      

    Examples: 
      Laugh:  You laugh.
              You laugh at Hailey.
              Hailey laughs.
              Hailey laughs at Saul.

      Lmao:   You laugh your ass off!
              You laugh your ass off at Hailey!
              Hailey laughs their ass off!
              Hailey laughs their ass off at Saul!

      Lol:    You laugh out loud.
              You laugh out loud at Hailey.
              Hailey laughs out loud.
              Hailey laughs out loud at Saul.

      Rofl:   You roll on the floor, laughing!
              You roll on the floor, laughing at Hailey!
              Hailey rolls on the floor, laughing!
              Hailey rolls on the floor, laughing at Saul!
    """

    key = "laugh"
    aliases = ["lmao", "lol", "rofl"]
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None
        punctuation = "."

        self_msg = "You laugh "
        room_msg = f"{caller.name} laughs "
        target_msg = f"{caller.name} laughs "

        if self.cmdstring == "lmao":
            self_msg += "your ass off "
            room_msg += "their ass off "
            target_msg += "their ass off "
            punctuation = "!"
        elif self.cmdstring == "lol":
            self_msg += "out loud "
            room_msg += "out loud "
            target_msg += "out loud "
        elif self.cmdstring == "rofl":
            self_msg = "You roll on the floor, laughing "
            room_msg = f"{caller.name} rolls on the floor, laughing "
            target_msg = f"{caller.name} rolls on the floor, laughing "
            punctuation = "!"

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation=punctuation)

class CmdLeer(Social):
    """
    Syntax: leer

    Examples: You leer at everyone.
              You leer at Hailey.

              Hailey leers at everyone.
              Hailey leers at Saul.
              Hailey leers at you.
    """

    key = "leer"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You leer "
        room_msg = f"{caller.name} leers "
        target_msg = f"{caller.name} leers "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "
        elif target == caller:
            self_msg += "at yourself "
            room_msg += "at themselves "
        elif not extra:
            self_msg += "at everyone "
            room_msg += "at everyone "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdMoan(Social):
    """
    Syntax: moan

    Examples: You moan.
              You moan at Hailey.

              Hailey moans.
              Hailey moans at Saul.
              Hailey moans at you.
    """

    key = "moan"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You moan "
        room_msg = f"{caller.name} moans "
        target_msg = f"{caller.name} moan "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdMuse(Social):
    """
    Syntax: muse

    Examples: You muse in thought.

              Hailey muses in thought.
    """

    key = "muse"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You muse in thought."
        room_msg = f"{caller.name} muses in thought."

        caller.at_social(self_msg, room_msg, extra=None)

class CmdMutter(Social):
    """
    Syntax: mutter

    Examples: You mutter under your breath.
              You mutter bitter things about Hailey.

              Hailey mutters under their breath.
              Hailey mutters bitter things about Saul.
              Hailey mutters bitter things about you.
    """

    key = "mutter"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You mutter "
        room_msg = f"{caller.name} mutters "
        target_msg = f"{caller.name} mutters "

        if target and not target == caller:
            self_msg += f"bitter things about {target.name} "
            room_msg += f"bitter things about {target.name} "
            target_msg += "bitter things about you "
        else:
            self_msg += "under your breath."
            room_msg += "under their breath "

        caller.at_social(self_msg, room_msg, target_msg, target, extra=None)

class CmdNibble(Social):
    """
    Syntax: nibble

    Examples: You nibble on your lower lip.
              You nibble on Hailey's ear.

              Hailey nibbles on their lower lip.
              Hailey nibbles on Saul's ear.
              Hailey nibbles on your ear.
    """

    key = "nibble"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You nibble "
        room_msg = f"{caller.name} nibbles "
        target_msg = f"{caller.name} nibbles "

        if (not target or target == caller) and not extra:
            self_msg += "on your lower lip "
            room_msg += "on their lower lip "
        elif (not target or target == caller) and extra:
            self_msg += "on your "
            room_msg += "on their "
        elif target:
            self_msg += f"on {target.name}'s "
            room_msg += f"on {target.name}'s "
            target_msg += f"on your "
            if not extra:
                self_msg += "ear "
                room_msg += "ear "
                target_msg += "ear "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdNod(Social):
    """
    Syntax: nod

    Examples: You nod.
              You nod at Hailey.

              Hailey nods.
              Hailey nods at Saul.
              Hailey nods at you.
    """

    key = "nod"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You nod "
        room_msg = f"{caller.name} nods "
        target_msg = f"{caller.name} nods "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdNudge(Social):
    """
    Syntax: nudge

    Examples: You nudge everyone.
              You nudge Hailey.

              Hailey nudges everyone.
              Hailey nudges Saul.
              Hailey nudges you.
    """

    key = "nudge"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You nudge "
        room_msg = f"{caller.name} nudges "
        target_msg = f"{caller.name} nudges "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
        elif not target:
            self_msg += "everyone "
            room_msg += "everyone "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdNuzzle(Social):
    """
    Syntax: nuzzle

    Examples: You nuzzle Hailey affectionately.

              Hailey nuzzles Saul affectionately.
              Hailey nuzzles you affectionately.
    """

    key = "nuzzle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if not target:
            caller.msg("Nuzzle who?")
            return
        elif target == caller:
            self_msg = "You raise your own hand and nuzzle it."
            room_msg = f"{caller.name} raises their own hand and nuzzles it."
            caller.at_social(self_msg, room_msg, extra=None)
            return
        else:
            self_msg = f"You nuzzle {target.name} "
            room_msg = f"{caller.name} nuzzles {target.name} "
            target_msg = f"{caller.name} nuzzles you "

        if not extra:
            self_msg += "affectionately "
            room_msg += "affectionately "
            target_msg += "affectionately "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPace(Social):
    """
    Syntax: pace

    Examples: You pace.
              You pace around Hailey.

              Hailey paces.
              Hailey paces around Saul.
              Hailey paces around you.
    """

    key = "pace"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pace "
        room_msg = f"{caller.name} paces "
        target_msg = f"{caller.name} paces "

        if target and not target == caller:
            self_msg += f"around {target.name} "
            room_msg += f"around {target.name} "
            target_msg += "around you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPanic(Social):
    """
    Syntax: panic

    Examples: You panic.
              You panic about Hailey.

              Hailey panics.
              Hailey panics about Saul.
              Hailey panics about you.
    """

    key = "panic"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You panic "
        room_msg = f"{caller.name} panics "
        target_msg = f"{caller.name} panics "

        if target and not target == caller:
            self_msg += f"about {target.name} "
            room_msg += f"about {target.name} "
            target_msg += "about you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPant(Social):
    """
    Syntax: pant

    Examples: You pant for breath.
              You pant heavily.

              Hailey pants for breath.
              Hailey pants heavily.
    """

    key = "pant"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pant "
        room_msg = f"{caller.name} pants "
        target_msg = f"{caller.name} pants "

        if not extra:
            self_msg += "for breath "
            room_msg += "for breath "
        

        caller.at_social(self_msg, room_msg, extra=extra)

class CmdPat(Social):
    """
    Syntax: pat

    Examples: You pat Hailey.

              Hailey pats Saul.
              Hailey pats you.
    """

    key = "pat"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pat "
        room_msg = f"{caller.name} pats "
        target_msg = f"{caller.name} pats "

        if not target:
            caller.msg("Pat who?")
            return
        elif target == caller:
            self_msg += "yourself "
            room_msg += f"themselves "
            if not extra:
                self_msg += "down "
                room_msg += "down "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPet(Social):
    """
    Syntax: pet

    Examples: You pet Hailey.

              Hailey pets Saul.
              Hailey pets you.
    """

    key = "pet"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pet "
        room_msg = f"{caller.name} pets "
        target_msg = f"{caller.name} pets "

        if not target:
            caller.msg("Pet who?")
            return
        elif target == caller:
            self_msg = "You reach up to pet yourself like some sort of sociopath "
            room_msg = f"{caller.name} reaches up to pet themselves like some sort of sociopath "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPeer(Social):
    """
    Syntax: peer

    Examples: You peer at everyone.
              You peer at Hailey.

              Hailey peers at everyone.
              Hailey peers at Saul.
              Hailey peers at you.
    """

    key = "peer"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You peer "
        room_msg = f"{caller.name} peers "
        target_msg = f"{caller.name} peers "

        if not target:
            self_msg += "at everyone "
            room_msg += "at everyone "
        elif target == caller:
            self_msg += "at yourself. Suspicious..."
            room_msg += "at themselves. Suspicious..."
            caller.at_social(self_msg, room_msg)
            return
        else:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPinch(Social):
    """
    Syntax: pinch

    Examples: You pinch yourself.
              You pinch Hailey.

              Hailey pinches themselves.
              Hailey pinches Saul.
              Hailey pinches you.
    """

    key = "pinch"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pinch "
        room_msg = f"{caller.name} pinches "
        target_msg = f"{caller.name} pinches "

        if not target or target == caller:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
            else:
                self_msg += "your "
                room_msg += "their "
        else:
            if not extra:
                self_msg += f"{target.name} "
                room_msg += f"{target.name} "
                target_msg += "you "
            else:
                self_msg += f"{target.name}'s "
                room_msg += f"{target.name}'s "
                target_msg += "your "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPlead(Social):
    """
    Syntax: plead

    Examples: You plead for your life.
              You plead Hailey.

              Hailey pleads for their life.
              Hailey pleads Saul.
              Hailey pleads you.
    """

    key = "plead"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You plead "
        room_msg = f"{caller.name} pleads "
        target_msg = f"{caller.name} pleads "

        if not target and not extra:
            self_msg += "for your life "
            room_msg += "for their life "
        elif target == caller:
            self_msg += "with yourself "
            room_msg += "with themselves "
            if not extra:
                self_msg += "for sweet release "
                room_msg += "for sweet release "
        elif target:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPoint(Social):
    """
    Syntax: point

    Examples: You point.
              You point at Hailey.

              Hailey points.
              Hailey points at Saul.
              Hailey points at you.
    """

    key = "point"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You point "
        room_msg = f"{caller.name} points "
        target_msg = f"{caller.name} points "

        if target:
            if target == caller:
                self_msg += "at yourself "
                room_msg += "at themselves "
            else:
                self_msg += f"at {target.name} "
                room_msg += f"at {target.name} "
                target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPoke(Social):
    """
    Syntax: poke

    Examples: You poke everyone.
              You pokes Hailey.

              Hailey pokes everyone.
              Hailey pokes Saul.
              Hailey pokes you.
    """

    key = "poke"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You poke "
        room_msg = f"{caller.name} pokes "
        target_msg = f"{caller.name} pokes "

        if not target:
            if not extra:
                self_msg += "everyone "
                room_msg += "everyone "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPonder(Social):
    """
    Syntax: ponder

    Examples: You ponder.
              You ponder Hailey.

              Hailey ponders.
              Hailey ponders Saul.
              Hailey ponders you.
    """

    key = "ponder"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You ponder "
        room_msg = f"{caller.name} ponders "
        target_msg = f"{caller.name} ponders "

        if target:
            if target == caller:
                if not extra:
                    self_msg += "yourself "
                    room_msg += "themselves "
                else:
                    self_msg += "your "
                    room_msg += "their "
            else:
                if not extra:
                    self_msg += f"{target.name} "
                    room_msg += f"{target.name} "
                    target_msg += "you "
                else:
                    self_msg += f"{target.name}'s "
                    room_msg += f"{target.name}'s "
                    target_msg += "your "


        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPounce(Social):
    """
    Syntax: pounce

    Examples: You ready to pounce!
              You pounce on Hailey!

              Hailey readies to pounce!
              Hailey pounces on Saul!
              Hailey pounces on you!
    """

    key = "pounce"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pounce "
        room_msg = f"{caller.name} pounces "
        target_msg = f"{caller.name} pounces "

        if not target:
            if not extra:
                self_msg = "You ready to pounce "
                room_msg = f"{caller.name} readies to pounce "
                caller.at_social(self_msg, room_msg, extra=None, punctuation='!')
                return
        elif target == caller:
            #potentially something for furry races?
            caller.msg("You cannot pounce on yourself.")
            return
        else:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation='!')

class CmdPout(Social):
    """
    Syntax: pout

    Examples: You pout.
              You pout at Hailey.

              Hailey pouts.
              Hailey pouts at Saul.
              Hailey pouts at you.
    """

    key = "pout"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You pout "
        room_msg = f"{caller.name} pouts "
        target_msg = f"{caller.name} pouts "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPuke(Social):
    """
    Syntax:  puke
    Aliases: vomit

    Examples: You puke.
              You puke on Hailey.
              Hailey pukes.
              Hailey pukes on Saul.
              Hailey pukes on you.

              You vomit into a lumpy puddle on the floor.
              Hailey vomits into a lumpy puddle on the floor.
    """

    key = "puke"
    aliases = ['vomit']
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if self.cmdstring == "vomit":
            self_msg = "You vomit into a lumpy puddle on the floor."
            room_msg = f"{caller.name} vomits into a lumpy puddle on the floor."
            caller.at_social(self_msg, room_msg, extra=None)
            return

        self_msg = "You puke "
        room_msg = f"{caller.name} pukes "
        target_msg = f"{caller.name} pukes "

        if target:
            if target == caller:
                self_msg += "on yourself "
                room_msg += "on themselves "
            else:
                self_msg += f"on {target.name} "
                room_msg += f"on {target.name} "
                target_msg += "on you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdPurr(Social):
    """
    Syntax: purr

    Examples: You purr.
              You purr at Hailey.

              Hailey purrs.
              Hailey purrs at Saul.
              Hailey purrs at you.
    """

    key = "purr"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You purr "
        room_msg = f"{caller.name} purrs "
        target_msg = f"{caller.name} purrs "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdQuiver(Social):
    """
    Syntax: quiver

    Examples: You quiver.

              Hailey quivers.
    """

    key = "quiver"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You quiver "
        room_msg = f"{caller.name} quivers "

        caller.at_social(self_msg, room_msg, extra=extra)

class CmdRoll(Social):
    """
    Syntax: roll

    Examples: You roll your eyes.
              You roll your eyes at Hailey.

              Hailey rolls their eyes.
              Hailey rolls their eyes at Saul.
              Hailey rolls their eyes at you.
    """

    key = "roll"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You roll "
        room_msg = f"{caller.name} rolls "
        target_msg = f"{caller.name} rolls "

        if not target:
            if not extra:
                self_msg += "your eyes "
                room_msg += "their eyes "
        elif target == caller:
            self_msg += "over on the floor "
            room_msg += "over on the floor "
        else:
            self_msg += f"your eyes at {target.name} "
            room_msg += f"their eyes at {target.name} "
            target_msg += "their eyes at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdRub(Social):
    """
    Syntax: rub

    Examples: You rub yourself.
              You rub Hailey.

              Hailey rubs themselves.
              Hailey rubs Saul.
              Hailey rubs you.
    """

    key = "rub"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You rub "
        room_msg = f"{caller.name} rubs "
        target_msg = f"{caller.name} rubs "

        if not target:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
        elif target == caller:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
            else:
                self_msg += "your "
                room_msg += "their "
        else:
            if not extra:
                self_msg += f"{target.name} "
                room_msg += f"{target.name} "
                target_msg += "you "
            else:
                self_msg += f"{target.name}'s "
                room_msg += f"{target.name}'s "
                target_msg += "your "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdRuffle(Social):
    """
    Syntax: ruffle

    Examples: You ruffle your hair.
              You ruffle Hailey's hair.

              Hailey ruffles their hair.
              Hailey ruffles Saul's hair.
              Hailey ruffles your hair.
    """

    key = "ruffle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You ruffle "
        room_msg = f"{caller.name} ruffles "
        target_msg = f"{caller.name} ruffles "

        if not target or target == caller:
            self_msg += "your "
            room_msg += "their "
            if not extra:
                self_msg += "hair "
                room_msg += "hair "
        else:
            self_msg += f"{target.name}'s " 
            room_msg += f"{target.name}'s "
            target_msg += "your "
            if not extra:
                self_msg += "hair "
                room_msg += "hair "
                target_msg += "hair "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)
      
class CmdScowl(Social):
    """
    Syntax: scowl

    Examples: You scowl.
              You scowl at Hailey.

              Hailey scowls.
              Hailey scowls at Saul.
              Hailey scowls at you.
    """

    key = "scowl"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You scowl "
        room_msg = f"{caller.name} scowls "
        target_msg = f"{caller.name} scowls "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdScratch(Social):
    """
    Syntax: scratch

    Examples: You scratch your head.
              You scratch Hailey.

              Hailey scratches their head.
              Hailey scratches Saul.
              Hailey scratches you.
    """

    key = "scratch"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You scratch "
        room_msg = f"{caller.name} scratches "
        target_msg = f"{caller.name} scratches "

        if not target:
            if not extra:
                self_msg += "your head "
                room_msg += "their head "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdScream(Social):
    """
    Syntax: scream

    Examples: You scream!
              You scream at Hailey!

              Hailey scream!
              Hailey screams at Saul!
              Hailey screams at you!
    """

    key = "scream"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You scream "
        room_msg = f"{caller.name} screams "
        target_msg = f"{caller.name} screams "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation='!')

class CmdShake(Social):
    """
    Syntax: shake

    Examples: You shake your head.
              You shake your head at Hailey.

              Hailey shakes their head.
              Hailey shakes their head at Saul.
              Hailey shakes their head at you.
    """

    key = "shake"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You shake your head "
        room_msg = f"{caller.name} shakes their head "
        target_msg = f"{caller.name} shakes their head "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdShiver(Social):
    """
    Syntax: shiver

    Examples: You shiver.

              Hailey shivers.
    """

    key = "shiver"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You shiver "
        room_msg = f"{caller.name} shivers "

        caller.at_social(self_msg, room_msg, extra=extra)

class CmdShrug(Social):
    """
    Syntax: shrug

    Examples: You shrug.
              You shrug at Hailey.

              Hailey shrugs.
              Hailey shrugs at Saul.
              Hailey shrugs at you.
    """

    key = "shrug"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You shrug "
        room_msg = f"{caller.name} shrugs "
        target_msg = f"{caller.name} shrugs "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdShudder(Social):
    """
    Syntax: shudder

    Examples: You shudder.

              Hailey shudders.
    """

    key = "shudder"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You shudder "
        room_msg = f"{caller.name} shudders "

        caller.at_social(self_msg, room_msg, extra=None)

class CmdShuffle(Social):
    """
    Syntax: shuffle

    Examples: You shuffle about uncomfortably.

              Hailey shuffles about uncomfortably.
    """

    key = "shuffle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You shuffle about uncomfortably "
        room_msg = f"{caller.name} shuffles about uncomfortably "

        caller.at_social(self_msg, room_msg, extra=None)

class CmdSit(Social):
    """
    Syntax: sit

    Examples: You sit.
              You sit on Hailey.

              Hailey sits.
              Hailey sits on Saul.
              Hailey sits on you.
    """

    key = "sit"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You sit "
        room_msg = f"{caller.name} sits "
        target_msg = f"{caller.name} sits "

        if target and not target == caller:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSlap(Social):
    """
    Syntax:  slap
    Aliases: bslap

    Examples: You slap yourself.
              You slap Hailey.
              Hailey slaps herself.
              Hailey slaps Saul.
              Hailey slaps you.

              You bitchslap yourself.
              You bitchslap Hailey.
              Hailey bitchslaps herself.
              Hailey bitchslaps Saul.
              Hailey bitchslaps you.
    """

    key = "slap"
    aliases = ["bslap"]
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if self.cmdstring == "slap":
            self_msg = "You slap "
            room_msg = f"{caller.name} slaps "
            target_msg = f"{caller.name} slaps "
        elif self.cmdstring == "bslap":
            self_msg = "You bitchslap "
            room_msg = f"{caller.name} bitchslaps "
            target_msg = f"{caller.name} bitchslaps "

        if not target or target == caller:
            self_msg += f"yourself "
            room_msg += f"themselves "
            target_msg += f"themselves "
        elif target:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSmack(Social):
    """
    Syntax: smack

    Examples: You smack yourself.
              You smack Hailey.

              Hailey smacks themselves.
              Hailey smacks Saul.
              Hailey smacks you.
    """

    key = "smack"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You smack "
        room_msg = f"{caller.name} smacks "
        target_msg = f"{caller.name} smacks "

        if not target:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSmile(Social):
    """
    Syntax: smile

    Examples: You smile.
              You smile at Hailey.

              Hailey smiles.
              Hailey smiles at Saul.
              Hailey smiles at you.
    """

    key = "smile"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You smile "
        room_msg = f"{caller.name} smiles "
        target_msg = f"{caller.name} smiles "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSmirk(Social):
    """
    Syntax: smirk

    Examples: You smirk.
              You smirk at Hailey.

              Hailey smirks.
              Hailey smirks at Saul.
              Hailey smirks at you.
    """

    key = "smirk"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You smirk "
        room_msg = f"{caller.name} smirks "
        target_msg = f"{caller.name} smirks "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSmooch(Social):
    """
    Syntax: smooch

    Examples: You smooch Hailey.

              Hailey smooches Saul.
              Hailey smooches you.
    """

    key = "smooch"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You smooch "
        room_msg = f"{caller.name} smooches "
        target_msg = f"{caller.name} smooches "

        if not target:
            caller.msg("Smooch who?")
            return
        elif target == caller:
            self_msg = "the back of your hand "
            room_msg = "the back of their hand "
            caller.at_social(self_msg, room_msg, extra=None)
            return
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSnap(Social):
    """
    Syntax: snap

    Examples: You snap.
              You snap at Hailey.

              Hailey snaps.
              Hailey snaps at Saul.
              Hailey snaps at you.
    """

    key = "snap"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You snap "
        room_msg = f"{caller.name} snaps "
        target_msg = f"{caller.name} snaps "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSneer(Social):
    """
    Syntax: sneer

    Examples: You sneer.
              You sneer at Hailey.

              Hailey sneers.
              Hailey sneers at Saul.
              Hailey sneers at you.
    """

    key = "sneer"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You sneer "
        room_msg = f"{caller.name} sneers "
        target_msg = f"{caller.name} sneers "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSnicker(Social):
    """
    Syntax: snicker

    Examples: You snicker.
              You snicker at Hailey.

              Hailey snickers.
              Hailey snickers at Saul.
              Hailey snickers at you.
    """

    key = "snicker"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You snicker "
        room_msg = f"{caller.name} snickers "
        target_msg = f"{caller.name} snickers "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSniff(Social):
    """
    Syntax: sniff

    Examples: You sniff.
              You sniff Hailey.

              Hailey sniffs.
              Hailey sniffs Saul.
              Hailey sniffs you.
    """

    key = "sniff"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You sniff "
        room_msg = f"{caller.name} sniffs "
        target_msg = f"{caller.name} sniffs "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSniffle(Social):
    """
    Syntax: sniffle

    Examples: You sniffle.
              You sniffle at Hailey.

              Hailey sniffles.
              Hailey sniffles at Saul.
              Hailey sniffles at you.
    """

    key = "sniffle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You sniffle "
        room_msg = f"{caller.name} sniffles "
        target_msg = f"{caller.name} sniffles "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSnore(Social):
    """
    Syntax: snore

    Examples: You snore.
              You snore in Hailey's ear.

              Hailey snores.
              Hailey snores in Saul's ear.
              Hailey snores in your ear.
    """

    key = "snore"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You snore "
        room_msg = f"{caller.name} snores "
        target_msg = f"{caller.name} snores "


        if target and not target == caller:
            self_msg += f"in {target.name}'s ear "
            room_msg += f"in {target.name}'s ear "
            target_msg += "in your ear "

        caller.at_social(self_msg, room_msg, target_msg, target, extra=None)

class CmdSnort(Social):
    """
    Syntax: snort

    Examples: You snort.
              You snort at Hailey.

              Hailey snorts.
              Hailey snorts at Saul.
              Hailey snorts at you.
    """

    key = "snort"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You snort "
        room_msg = f"{caller.name} snorts "
        target_msg = f"{caller.name} snorts "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSnuggle(Social):
    """
    Syntax: snuggle

    Examples: You snuggle up to Hailey.

              Hailey snuggles up to Saul.
              Hailey snuggles up to you.
    """

    key = "snuggle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if not target:
            caller.msg("Snuggle with who?")
            return
        elif target == caller:
            self_msg = "You snuggle up with a blanket "
            room_msg = f"{caller.name} snuggles up with a blanket "
            caller.at_social(self_msg, room_msg, extra=None)
            return
        else:
            self_msg = f"You snuggle up to {target.name} "
            room_msg = f"{caller.name} snuggles up to {target.name} "
            target_msg = f"{caller.name} snuggles up to you "
            if not extra:
                self_msg += "affectionately "
                room_msg += "affectionately "
                target_msg += "affectionately "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSob(Social):
    """
    Syntax: sob

    Examples: You sob.
              You sob on Hailey's shoulder.

              Hailey sobs.
              Hailey sobs on Saul's shoulder.
              Hailey sobs on your shoulder.
    """

    key = "sob"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You sob "
        room_msg = f"{caller.name} sobs "
        target_msg = f"{caller.name} sobs "

        if target and not target == caller:
            self_msg += f"on {target.name}'s shoulder "
            room_msg += f"on {target.name}'s shoulder "
            target_msg += "on your shoulder "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSpank(Social):
    """
    Syntax: spank

    Examples: You spank yourself.
              You spank Hailey.

              Hailey spanks themselves.
              Hailey spanks Saul.
              Hailey spanks you.
    """

    key = "spank"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You spank "
        room_msg = f"{caller.name} spanks "
        target_msg = f"{caller.name} spanks "

        if not target or target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSpit(Social):
    """
    Syntax: spit

    Examples: You spit.
              You spit on Hailey.

              Hailey spits.
              Hailey spits on Saul.
              Hailey spits on you.
    """

    key = "spit"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You spit "
        room_msg = f"{caller.name} spits "
        target_msg = f"{caller.name} spits "

        if target and not target == caller:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSqueeze(Social):
    """
    Syntax: squeeze

    Examples: You squeeze yourself.
              You squeeze Hailey.

              Hailey squeezes themselves.
              Hailey squeezes Saul.
              Hailey squeezes you.
    """

    key = "squeeze"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You squeeze "
        room_msg = f"{caller.name} squeezes "
        target_msg = f"{caller.name} squeezes "

        if not target:
            if not extra:
                self_msg += "yourself fondly "
                room_msg += "themselves fondly "
        elif target == caller:
            if not extra:
                self_msg += "yourself fondly "
                room_msg += "themselves fondly "
            else:
                self_msg += "your "
                room_msg += "their "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "
            if not extra:
                self_msg += "fondly "
                room_msg += "fondly "
                target_msg += "fondly "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdStagger(Social):
    """
    Syntax: stagger

    Examples: You stagger.
              You stagger around Hailey.

              Hailey staggers.
              Hailey staggers around Saul.
              Hailey staggers around you.
    """

    key = "stagger"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stagger "
        room_msg = f"{caller.name} staggers "
        target_msg = f"{caller.name} staggers "

        if target and not target == caller:
            self_msg += f"around {target.name} "
            room_msg += f"around {target.name} "
            target_msg += "around you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdStamp(Social):
    """
    Syntax: stamp

    Examples: You stamp your foot.
              You stamp your foot at Hailey.

              Hailey stamps their foot.
              Hailey stamps their foot at Saul.
              Hailey stamps their foot at you.
    """

    key = "stamp"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stamp your foot "
        room_msg = f"{caller.name} stamps their foot "
        target_msg = f"{caller.name} stamps their foot "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdStand(Social):
    """
    Syntax: stand

    Examples: You stand.
              You stand near Hailey.

              Hailey stands.
              Hailey stands near Saul.
              Hailey stands near you.
    """

    key = "stand"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stand "
        room_msg = f"{caller.name} stands "
        target_msg = f"{caller.name} stands "

        if target and not target == caller:
            self_msg += f"near {target.name} "
            room_msg += f"near {target.name} "
            target_msg += "near you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdStare(Social):
    """
    Syntax: stare

    Examples: You stare.
              You stare at Hailey.

              Hailey stares.
              Hailey stares at Saul.
              Hailey stares at you.
    """

    key = "stare"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stare "
        room_msg = f"{caller.name} stares "
        target_msg = f"{caller.name} stares "

        if not target:
            if not extra:
                self_msg += "dreamily into space "
                room_msg += "dreamily into space "
        elif target == caller:
            caller.msg("You cannot stare at yourself.")
            return
        else:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdStifle(Social):
    """
    Syntax: stifle

    Examples: You stifle a giggle.

              Hailey stifles a giggle.
    """

    key = "stifle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stifle a giggle "
        room_msg = f"{caller.name} stifles a giggle "

        caller.at_social(self_msg, room_msg, extra=None)

class CmdStroke(Social):
    """
    Syntax: stroke

    Examples: You stroke yourself.
              You stroke Hailey.

              Hailey strokes themselves.
              Hailey strokes Saul.
              Hailey strokes you.
    """

    key = "stroke"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stroke "
        room_msg = f"{caller.name} strokes "
        target_msg = f"{caller.name} strokes "

        if not target:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdStomp(Social):
    """
    Syntax: stomp

    Examples: You stomp around angrily!
              You stomp on Hailey!

              Hailey stomps around angrily!
              Hailey stomps on Saul!
              Hailey stomps on you!
    """

    key = "stomp"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stomp "
        room_msg = f"{caller.name} stomps "
        target_msg = f"{caller.name} stomps "

        if not target:
            if not extra:
                self_msg += "around angrily "
                room_msg += "around angrily "
        elif target == caller:
            self_msg += "on your own foot "
            room_msg += "on your own foot "
        else:
            self_msg += f"on {target.name} "
            room_msg += f"on {target.name} "
            target_msg += "on you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra, punctuation='!')

class CmdStretch(Social):
    """
    Syntax: stretch

    Examples: You stretch out languidly.
              
              Hailey stretches out languidly.
    """

    key = "stretch"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stretch out "
        room_msg = f"{caller.name} stretches out "

        if not extra:
            self_msg += "languidly "
            room_msg += "languidly "

        caller.at_social(self_msg, room_msg, extra)

class CmdStrut(Social):
    """
    Syntax: strut

    Examples: You strut your stuff.
              
              Hailey struts their stuff.
    """

    key = "strut"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You strut "
        room_msg = f"{caller.name} struts "

        if not extra:
            self_msg += "your stuff "
            room_msg += "their stuff "

        caller.at_social(self_msg, room_msg, extra)

class CmdStumble(Social):
    """
    Syntax: stumble

    Examples: You stumble.
              You stumble around Hailey.

              Hailey stumbles.
              Hailey stumbles around Saul.
              Hailey stumbles around you.
    """

    key = "stumble"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stumble "
        room_msg = f"{caller.name} stumbles "
        target_msg = f"{caller.name} stumbles "

        if target and not target == caller:
            self_msg += f"around {target.name} "
            room_msg += f"around {target.name} "
            target_msg += "around you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdSulk(Social):
    #Written by Myrh.
    """
    Syntax: sulk

    Examples: You sulk petulantly.
              You sulk near Hailey petulantly.

              Hailey sulks petulantly.
              Hailey sulks near Saul petulantly.
              Hailey sulks near you petulantly.
    """

    key = "sulk"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You sulk "
        room_msg = f"{caller.name} sulks "
        target_msg = f"{caller.name} sulks "

        if target and not target == caller:
            self_msg += f"near {target.name} "
            room_msg += f"near {target.name} "
            target_msg += "near you "

        if not extra:
            self_msg += "petulantly "
            room_msg += "petulantly "
            target_msg += "petulantly "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTackle(Social):
    """
    Syntax: tackle

    Examples: You tackle Hailey.

              Hailey tackles Saul.
              Hailey tackles you.
    """

    key = "tackle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        if not target:
            caller.msg("Tackle who?")
            return
        elif target == caller:
            self_msg = "You tackle and wrestle yourself to the ground."
            room_msg = f"{caller.name} tackles and wrestles themselves to the ground."
            caller.at_social(self_msg, room_msg, extra=None)
            return
        else:
            self_msg = f"You tackle {target.name} "
            room_msg = f"{caller.name} tackles {target.name} "
            target_msg = f"{caller.name} tackles you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTap(Social):
    """
    Syntax: tap

    Examples: You tap your foot impatiently.
              You tap Hailey.

              Hailey taps their foot impatiently.
              Hailey taps Saul.
              Hailey taps you.
    """

    key = "tap"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You tap "
        room_msg = f"{caller.name} taps "
        target_msg = f"{caller.name} taps "

        if not target:
            if not extra:
                self_msg += "your foot impatiently "
                room_msg += "their foot impatiently "
        elif target == caller:
            self_msg += "your "
            room_msg += "their "
            if not extra:
                self_msg += "temple "
                room_msg += "temple "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTease(Social):
    """
    Syntax: tease

    Examples: You tease yourself.
              You tease Hailey.

              Hailey teases themselves.
              Hailey teases Saul.
              Hailey teases you.
    """

    key = "tease"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You tease "
        room_msg = f"{caller.name} teases "
        target_msg = f"{caller.name} teases "

        if not target:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdThank(Social):
    """
    Syntax: thank

    Examples: You thank everyone.
              You thank Hailey.

              Hailey thanks everyone.
              Hailey thanks Saul.
              Hailey thanks you.
    """

    key = "thank"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You thank "
        room_msg = f"{caller.name} thanks "
        target_msg = f"{caller.name} thanks "

        if not target:
            if not extra:
                self_msg += "everyone "
                room_msg += "everyone "
        elif target == caller:
            self_msg += "yourself "
            room_msg += "themselves "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdThink(Social):
    """
    Syntax: think

    Examples: You think.
              You think about Hailey.

              Hailey thinks.
              Hailey thinks around Saul.
              Hailey thinks around you.
    """

    key = "think"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You think "
        room_msg = f"{caller.name} thinks "
        target_msg = f"{caller.name} thinks "

        if target:
            if target == caller:
                self_msg += "about yourself "
                room_msg += "about themselves "
            else:
                self_msg += f"about {target.name} "
                room_msg += f"about {target.name} "
                target_msg += "about you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTickle(Social):
    """
    Syntax: tickle

    Examples: You tickle yourself.
              You tickle Hailey.

              Hailey tickles themselves.
              Hailey tickles Saul.
              Hailey tickles you.
    """

    key = "tickle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You tickle "
        room_msg = f"{caller.name} tickles "
        target_msg = f"{caller.name} tickles "

        if not target:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
        elif target == caller:
            if not extra:
                self_msg += "yourself "
                room_msg += "themselves "
            else:
                self_msg += "your "
                room_msg += "their "
        else:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTongue(Social):
    """
    Syntax: tongue

    Examples: You stick your tongue out.
              You stick your tongue out at Hailey.

              Hailey sticks their tongue out.
              Hailey sticks their tongue out at Saul.
              Hailey sticks their tongue out at you.
    """

    key = "tongue"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You stick your tongue out "
        room_msg = f"{caller.name} sticks their tongue out "
        target_msg = f"{caller.name} sticks their tongue out "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTremble(Social):
    """
    Syntax: tremble

    Examples: You tremble.

              Hailey trembles.
    """

    key = "tremble"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You tremble "
        room_msg = f"{caller.name} trembles "
        target_msg = f"{caller.name} trembles "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTsk(Social):
    """
    Syntax: tsk

    Examples: You tsk.
              You tsk at Hailey.

              Hailey tsks.
              Hailey tsks at Saul.
              Hailey tsks at you.
    """

    key = "tsk"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You tsk "
        room_msg = f"{caller.name} tsks "
        target_msg = f"{caller.name} tsks "

        if target:
            if target == caller:
                self_msg += "at yourself "
                room_msg += "at themselves "
            else:
                self_msg += f"at {target.name} "
                room_msg += f"at {target.name} "
                target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTwiddle(Social):
    """
    Syntax: twiddle

    Examples: You twiddle your thumbs.

              Hailey twiddles their thumbs.
    """

    key = "twiddle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You twiddle your thumbs "
        room_msg = f"{caller.name} twiddles their thumbs "

        caller.at_social(self_msg, room_msg, extra)

class CmdTwirl(Social):
    """
    Syntax: twirl

    Examples: You twirl around.
              You twirl Hailey around.

              Hailey twirls around.
              Hailey twirls Saul around.
              Hailey twirls you around.
    """

    key = "twirl"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You twirl "
        room_msg = f"{caller.name} twirl "
        target_msg = f"{caller.name} twirl "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        if not extra:
            self_msg += "around "
            room_msg += "around "
            target_msg += "around "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdTwitch(Social):
    """
    Syntax: twitch

    Examples: You twitch.
              You twitch at Hailey.

              Hailey twitches.
              Hailey twitches at Saul.
              Hailey twitches at you.
    """

    key = "twitch"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You twitch "
        room_msg = f"{caller.name} twitches "
        target_msg = f"{caller.name} twitches "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWait(Social):
    """
    Syntax: wait

    Examples: You wait.
              You wait for Hailey.

              Hailey waits.
              Hailey waits for Saul.
              Hailey waits for you.
    """

    key = "wait"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wait "
        room_msg = f"{caller.name} waits "
        target_msg = f"{caller.name} waits "

        if target and not target == caller:
            self_msg += f"for {target.name} "
            room_msg += f"for {target.name} "
            target_msg += "for you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWaltz(Social):
    """
    Syntax: waltz

    Examples: You waltz.
              You waltz with Hailey.

              Hailey waltzes.
              Hailey waltzes with Saul.
              Hailey waltzes with you.
    """

    key = "waltz"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You waltz "
        room_msg = f"{caller.name} waltzes "
        target_msg = f"{caller.name} waltzes "

        if target and not target == caller:
            self_msg += f"with {target.name} "
            room_msg += f"with {target.name} "
            target_msg += "with you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWave(Social):
    """
    Syntax: wave

    Examples: You wave.
              You wave at Hailey.

              Hailey waves.
              Hailey waves at Saul.
              Hailey waves at you.
    """

    key = "wave"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wave "
        room_msg = f"{caller.name} waves "
        target_msg = f"{caller.name} waves "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWhimper(Social):
    """
    Syntax: whimper

    Examples: You whimper.
              You whimper at Hailey.

              Hailey whimpers.
              Hailey whimpers at Saul.
              Hailey whimpers at you.
    """

    key = "whimper"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You whimper "
        room_msg = f"{caller.name} whimpers "
        target_msg = f"{caller.name} whimpers "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWiggle(Social):
    """
    Syntax: wiggle

    Examples: You wiggle your butt.
              You wiggle your butt at Hailey.

              Hailey wiggles your butt.
              Hailey wiggles your butt at Saul.
              Hailey wiggles your butt at you.
    """

    key = "wiggle"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wiggle your butt "
        room_msg = f"{caller.name} wiggles your butt "
        target_msg = f"{caller.name} wiggles your butt "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWince(Social):
    """
    Syntax: wince

    Examples: You wince.
              You wince at Hailey.

              Hailey winces.
              Hailey winces at Saul.
              Hailey winces at you.
    """

    key = "wince"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wince "
        room_msg = f"{caller.name} winces "
        target_msg = f"{caller.name} winces "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWipe(Social):
    """
    Syntax: wipe

    Examples: You wipe your hands off.
              You wipe your hands off on Hailey.

              Hailey wipes their hands off.
              Hailey wipes their hands off at Saul.
              Hailey wipes their hands off at you.
    """

    key = "wipe"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wipe "
        room_msg = f"{caller.name} wipes "
        target_msg = f"{caller.name} wipes "

        if not target:
            if not extra:
                self_msg += "your hands off "
                room_msg += "their hands off "
        elif target == caller:
            self_msg += "the sweat from your brow "
            room_msg += "the sweat from their brow "
        elif not extra:
            self_msg += f"your hands off on {target.name} "
            room_msg += f"their hands off on {target.name} "
            target_msg += "their hands off on you "
        else:
            self_msg += f"{target.name}'s "
            room_msg += f"{target.name}'s "
            target_msg += "your "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWonder(Social):
    """
    Syntax: wonder

    Examples: You wonder.
              You wonder about Hailey.

              Hailey wonders.
              Hailey wonders about Saul.
              Hailey wonders about you.
    """

    key = "wonder"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wonder "
        room_msg = f"{caller.name} wonders "
        target_msg = f"{caller.name} wonders "

        if target and not target == caller:
            self_msg += f"about {target.name} "
            room_msg += f"about {target.name} "
            target_msg += "about you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWorship(Social):
    """
    Syntax: worship

    Examples: You worship.
              You worship Hailey.

              Hailey worships.
              Hailey worships Saul.
              Hailey worships you.
    """

    key = "worship"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You worship "
        room_msg = f"{caller.name} worships "
        target_msg = f"{caller.name} worships "

        if target and not target == caller:
            self_msg += f"{target.name} "
            room_msg += f"{target.name} "
            target_msg += "you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdWow(Social):
    """
    Syntax: wow

    Examples: You wow at it all.
              You wow at Hailey.

              Hailey wows at it all.
              Hailey wows at Saul.
              Hailey wows at you.
    """

    key = "wow"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You wow "
        room_msg = f"{caller.name} wows "
        target_msg = f"{caller.name} wows "

        if not target:
            self_msg += "at it all "
            room_msg += "at it all "
        elif target == caller:
            self_msg += "at your own accomplishments "
            room_msg += "at their own accomplishments "
        else:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)

class CmdYawn(Social):
    """
    Syntax: yawn

    Examples: You yawn.
              You yawn at Hailey.

              Hailey yawns.
              Hailey yawns at Saul.
              Hailey yawns at you.
    """

    key = "yawn"
    locks = "cmd:all()"
    auto_help = False
    help_category = "Socials"

    def func(self):
        caller = self.caller
        target = self.target
        extra  = self.extra or None

        self_msg = "You yawn "
        room_msg = f"{caller.name} yawns "
        target_msg = f"{caller.name} yawns "

        if target and not target == caller:
            self_msg += f"at {target.name} "
            room_msg += f"at {target.name} "
            target_msg += "at you "

        caller.at_social(self_msg, room_msg, target_msg, target, extra)