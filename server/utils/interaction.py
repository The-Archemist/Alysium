from server.utils.utils import wrap

def dialogue(speaker, speech, speaker_color="|w"):
    """
    Create interactions.

    Arguments:
     Speaker       - Who is doing the speaking?
     Speech        - What are they saying?
     Speaker_color - XTERM code for color (optional)
    """

    speaker = speaker_color + str(speaker) + "|n: "
    speech  = wrap(speech, pre_text=speaker, indent=2)
    speech  = "\n" + speech
    return speech