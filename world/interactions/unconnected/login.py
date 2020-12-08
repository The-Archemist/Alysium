import re

from server.utils.interaction import dialogue
from server.utils.utils import wrap

from django.conf import settings
from evennia.utils.ansi import strip_ansi
from evennia.utils.utils import class_from_module

_ACCOUNT = class_from_module(settings.BASE_ACCOUNT_TYPECLASS)
_CHARACTER = class_from_module(settings.BASE_CHARACTER_TYPECLASS)

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
            caller.ndb._menutree.name = username
            caller.ndb._menutree.interaction = "intro_0"
            return "create_intro", {"username" : username}

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

_ENTRY = (
    "Welcome to |wAlysium|n!\n\n"

    "The following rules apply to names:\n"
    " - |CModern names are not allowed.|n (Ex: Hailey, Saul, John)\n"
    " - |CMythological names are not allowed.|n (Ex: Zeus, Hades, Hercules)\n"
    " - |CPopular literature names are not allowed.|n (Ex: Gandalf, Potter, Frodo)\n"
    " - |CDictionary words used for names are not allowed.|n (Ex: Death, Life, Love)\n\n"

    "Is {} correct and in adherence with the rules? |r(Y/N)|n\n"
)

_INTRO_1 = (
    "There is no light, no darkness. There is no cold or hot, no up or down, no life or death. This place is the absence of all things and the sheer and utter silence of that nothingness covers the expanse like a thick blanket.\n\n"

    "You could surrender; sink back into oblivion where it is easy, quiet, and peaceful. You wouldn't have to do anything any more.\n\n"

    "Ever.\n" 
)
            
_INTRO_2 = (
    "Yet amongst the muted grey tranquility, there is a discordant spark of chaos: the faintest heartbeat - a blip of existence.\n\n"

    "It is you.\n\n"

    "The thread of consciousness is tenuous and thin. You are just a dream of a dream, the precursor of being.\n\n"

    "A rare few veins flicker to life, beckoning you to rise.\n\n"
    
    "Are you male or female?\n"
)

_RACE_1 = (
    "The limbed and headed being that you are, disoriented and alone, is beginning to wake.\n\n"

    "You cannot see yourself. In the great aether exists no more than the outline of a {}. Suddenly, the realization is made: you have no memory of the face that awaits you underneath the coalescing wisps of shadow.\n\n"

    "All recollection of this person has been wiped away - the people and the world once familiar now drowned by primordial sea.\n\n" 

    "What are you?\n"
)


def create_username(caller, raw_text, **kwargs):
    """
    Prompt for character name confirmation.
    """

    def _check_input(caller, response, **kwargs):
        response = response.rstrip("\n")[0]
        if response.upper() == "Y":
            caller.ndb._menutree.name = kwargs['username']
            caller.ndb._menutree.interaction = "intro_0"
            return "create_password", {"username" : username}
        elif response.upper() == "N":
            return "login_username", {}
        else:
            return "create_username", kwargs

    username = kwargs['username']
    text = _ENTRY.format(username)
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

        if not account:
            for error in errors:
                session.msg(f"{error}")
            
            kwargs["retry_password"] = True
            return "create_password", kwargs

        return "create_intro", {"account" : account}

    text = "Enter a password:"
    options = (
        {"key" : "", "goto" : "login_username"},
        {"key" : ("quit", "q"), "goto" : "login_quit"},
        {"key" : "_default", "goto" : (_check_input, kwargs)}
    )

    return text, options

def create_intro(caller, raw_text, **kwargs):
    """
    Introduce Alysium.
    """
    
    interaction = caller.ndb._menutree.interaction 
    if interaction == "intro_0":
        interaction = "intro_1"
        speaker = "Alysium"
        caller.msg(dialogue(speaker, _INTRO_1))
        #caller.msg(wrap(_INTRO_1, pre_text=speaker, indent=2))

    def _assign_sex(caller, response, **kwargs):
        response = response.rstrip('\n').lower()
        if response in ("1", "male"):
            caller.ndb._menutree.sex = "male"
        elif response in ("2", "female"):
            caller.ndb._menutree.sex = "female"
        else:
            return "create_intro", kwargs

        caller.ndb._menutree.interaction = "race_0"
        return "create_race", kwargs

    def _parts(caller, response, **kwargs):
        name = caller.ndb._menutree.name
        response = response.rstrip("\n")
        if response == "1":
            speaker = "You"
            speech = "Never ever?"
            caller.msg(dialogue(speaker, speech))
            #speech = wrap(speech, pre_text=speaker, indent=2)
            #caller.msg("\n")
            #caller.msg(speaker)
            #caller.msg(speech)

            speaker = "Alysium"
            speech = f"Never ever ever, {name}."
            caller.msg(dialogue(speaker, speech))
            #speech = wrap(speech, pre_text=speaker, indent=2)
            #caller.msg(speaker)
            #caller.msg(speech)
        elif response == "2":
            caller.ndb._menutree.interaction = "intro_2"
            speaker = "Alysium"
            #caller.msg("\n")
            #caller.msg(speaker)
            caller.msg(dialogue(speaker, _INTRO_2))
            #caller.msg(wrap(_INTRO_2, pre_text=speaker, indent=2))

        return "create_intro", kwargs

    if interaction == "intro_1":
        text = """
            |n 1. - |045Never ever?
            |n 2. - |045(Simply keep on non-existing).|n
        """
        options = (
            {"key" : "",            "goto" : "create_sex"},
            {"key" : ("quit", "q"), "goto" : "login_quit"},
            {"key" : "_default",    "goto" : (_parts, kwargs)}
        )
    elif interaction == "intro_2":
        text = """
            |n 1. - |045Male
            |n 2. - |045Female|n
        """

        options = (
            {"key" : "",            "goto" : "create_sex"},
            {"key" : ("quit", "q"), "goto" : "login_quit"},
            {"key" : "_default",    "goto" : (_assign_sex, kwargs)}
        )

    caller.ndb._menutree.interaction = interaction
    return text, options

def create_race(caller, raw_text, **kwargs):
    """
    Prompt for racial selection.
    """
    _HUMAN = (
        "Politically-fractured societies gave way to mankind's centuries of war. Rebellions stood against treasonous monarchs. Peasants rose up against nobility. Civil wars scoured the lands, and it was not until well past the first age that humans began to set aside their hierarchical differences under the racially uniting banner of imperialism. Squabbling kingdoms were conquered one by one until the humans established a universal trade. Revanwood became the commercial hub of the world, and immigration quickly began to welcome even those from Alysium's farthest reaches.\n\n"

        "In the time since, most have taken to small cottages scattered along the countryside or houses within city districts. Only the nobility are privileged enough to merit chambers within the Revanwood Castle.\n\n"

        "By and large, modern day humans are considered abstract thinkers. They are compelled by an affinity for logic, a love for knowledge, and an innate greed for wealth. As such, many live out their days, expanding the frontiers of theology, philosophy, art, war, and commerce. Many believe their fleeting life is best spent on a conquest for prestige and any means by which to accrue it.\n"
    )

    _ELF = (
        ""
    )

    _DWARF = (
        ""
    )

    _DEORA = (
        "Dark elves (commonly, Deora) were not always seen as separate from their pale-skinned counterparts. Once upon a time, all elvenkind were simply that. On the sixty-second day of the Second Age (March 3rd, 1000) archaic gods reached down and set upon the elves a curse. One in every three should bear the mark of darkness, and so it was that a third of the population became charcoal grey and was lost of their graceful immortality.\n\n"

        "The first of the Deora turned to the Goddess of Night, Katla, pleading for answers to their sudden ailments. Katla told them that as she sat upon the stars, overseeing the eventide, she saw the elves conjure magics to steal from the sky and pluck from its tapestry pearly dusk to do with as they place. It angered the gods greatly for the arrogance of elves to escalate to a degree by which they'd dare oppose divine power and wield it as their own.\n\n"

        "Since their exile, the Deora have grown a contempt for all races beyond their own. In the centuries since, all others are regarded as outsiders and scorned for their existence. Extinction has threatened the ashen elves for years now, and it is estimated that they shall diminish entirely by the Third Age. Until then, these people have grown devoted to doing all in their power to share in their burdens. Assassinations, black markets, slavery, and dark sorcerery are but only a few tokens commonly accredited to the Deora. Whether or not such matters are factual does not inhibit their zeal to be accreditted.\n"
    )

    _LYKOS = (
        "It is said that, prior to the great creator's slumber, he took a pause and admired how creation had developed a death-defying love for the wildlife that surrounded the sentients. Bonds had sprouted between animals and those who took care of them in a degree that surpassed the affection either often had for even their own kind. It was by such loyalty and companionship that the creator saw it fit to dispel the greatest barrier separating humankind from the canines and felines who they cherished. Pleased, the creator gave both the gift of language.\n\n"

        "As is the age-old rivalry, canines and felines have always exhibited a deep contempt for one another. Either are bound to pine endlessly for the affection, companionship, and favoritism of their longest held friendships, so much so that neither can much stand the other's company.\n\n"

        "As for the lykan, the creator commanded humankind to teach and support the wolf-kin until they could develop a self-sustaining community of their own. Hundreds of years have since passed and the lykan have taken to familiar territory: the great woodlands of Alysium, but even still there is not a matter under the sun that could divide humankind from their best friend. It is only now that they have surpassed a domesticated relationship and exist as symbiotic allies.\n\n"

        "Most often, lykan are found in militaristic capacities or as agricultural farmers. Many characteristics are unlikely to change; fur, triangular-shaped head, ears both pointy and floppy, the digitigrade patterns that adorn them all remain, but apart from the gift of language the lykan have been given one additional blessing. Two friends may now grow old, one day reminisce of youthful days when times were simpler, and welcome death together as companions start to finish.\n"
    )

    _NYMPH = (
        "In the beginning, Old Gods roamed the land in a time untouched, unsoiled, and lost to the ages. Great energy surged everywhere, and it was then that Alysium's first children were born - the nymphs. Fae-touched, and often akin to the gods themselves, they were creatures of great beauty and mystery. They were the first and, to their culture, the greatest.\n\n"

        "Yet the nymphs never rose to political power. No stunning cities were built nor kingdoms to weather the trials of time, and nymphs certainly lacked the unity of the elves. There was no drive in them for further excellence - for how can you improve perfection? Unlike the races of the lesser, the nymphs hold an understanding that they are created, each and every one, as an image of purity. Thus, they lived a contented, self-fulfilled life.\n\n"

        "They were like wind - ever changing, ever moving, and, as time went on, they became well known for their migratory lifestyle, oft free-spirited and utilizing their superiority in the arts or magics to live as transcendentalists. Few have ever been able to compete with their angelic voices and gentle hands. Such closeness with nature has left the typical nymph heavily superstitious. They venerate the higher powers and have seen first-hand the doom that might befall any who forget the old ways. Insulting the gods or the lands in front of nymphs will always lead to quiet mutterings and the tossing of salt to ward away the evil such might bring. Despite this, they also tend to be exceptionally friendly hosts - at times, even childlike in their excitable dispositions. Their rules of bread-breaking are simple: be the most optimistic companion even when traveling on a cold winter night.\n\n"

        "Given their heritage - that of gods and of elements - some may bear unusual features. As the ancient ones have became the trees, the seas, the lands, as much is reflected upon their kin. A sea nymph might have cerulean skin and bright cyan eyes; one of the forests might be born with green flesh and an affinity with animals, sometimes even speaking with them as one does a friend. Regardless of their individual features, their heights do not often exceed five feet, and it is a snowy summer when one finds a nymph anything heartier than petite.\n"
    )

    _FELINE = (
        ""
    )

    _HALFLING = (
        ""
    )

    def _races(caller, race, **kwargs):
        race = race.rstrip('\n').lower()
        if race in ("1", "human"):
            speaker = "Human"
            caller.msg(dialogue(speaker, _HUMAN))
        elif race in ("2", "elf"):
            speaker = "Elf"
            caller.msg(dialogue(speaker, _ELF, "|C"))
        elif race in ("3", "deora", "dark elf"):
            speaker = "Deora"
            caller.msg(dialogue(speaker, _DEORA, "|x"))
        elif race in ("4", "dwarf"):
            speaker = "Dwarf"
            caller.msg(dialogue(speaker, _DWARF, "|Y"))
        elif race in ("5", "lykos", "dog"):
            speaker = "Lykos"
            caller.msg(dialogue(speaker, _LYKOS, "|G"))
        elif race in ("6", "nymph", "fae"):
            speaker = "Nymph"
            caller.msg(dialogue(speaker, _NYMPH, "|c"))
        elif race in ("7", "feline", "cat"):
            speaker = "Feline"
            caller.msg(dialogue(speaker, _FELINE, "|y"))
        elif race in ("8", "halfling"):
            speaker = "Halfling"
            caller.msg(dialogue(speaker, _HALFLING, "|g"))

        #potentially make dark elves a subrace?
        #elif race in ("3", "dark elf", "dark"):
        #    speaker = "Dark Elf"
        #    caller.msg(dialogue(speaker, _DARK_ELF, "|x"))

        caller.ndb._menutree.interaction = "race_1"
        return "create_race", kwargs
            
    sex = caller.ndb._menutree.sex 
    interaction = caller.ndb._menutree.interaction
    if interaction == "race_0":
        interaction = "race_1"
        speaker = "Alysium"
        caller.msg(dialogue(speaker, _RACE_1.format(sex)))
        #caller.msg(wrap(_RACE_1.format(sex), pre_text=speaker, indent=2))

    if interaction == "race_1":
        text = """
            |n 1. - |045Human
            |n 2. - |045Elf
            |n 3. - |045Deora
            |n 4. - |045Dwarf
            |n 5. - |045Lykos
            |n 6. - |045Nymph
            |n 7. - |045Feline
            |n 8. - |045Halfling|n
        """

        options = (
            {"key" : "",            "goto" : "create_sex"},
            {"key" : ("quit", "q"), "goto" : "login_quit"},
            {"key" : "_default",    "goto" : (_races, kwargs)}
        )

    return text, options

def create_check(caller, raw_text, **kwargs):
    #caller.msg(caller.db.all)
    return "", {}

def create_login(caller, raw_text, **kwargs):
    """
    Exit creation, login.
    """
    session = caller
    account = kwargs.get("account")
    session.sessionhandler.login(session, account)
    
    #assign databased variables upon login.
    character = account.db._last_puppet
    character.db.sex  = caller.db.sex
    character.db.race = caller.db.race

    return "", {}

