import re
import textwrap
from django.conf import settings
from evennia.utils.ansi import strip_ansi
from evennia.utils.utils import to_str

def wrap(text, width = None, pre_text = None, indent = 0):
    """
    Safely wrap text to a certain number of characters.

    Args:
        text (str): The text to wrap.
        width (int, optional): The number of characters to wrap to.
        indent (int): How much to indent each line (with whitespace).

    Returns:
        text (str): Properly wrapped text.

    Note: Could probably be optimized with a while loop.

    """
    width = width if width else settings.CLIENT_DEFAULT_WIDTH

    if not text:
        return ""

    if pre_text:
        indent = len(pre_text)

    #split user-defined paragraphs into separate arrays.
    paragraphs = re.split(r"\n|\|/", text)
    for paragraph in paragraphs:
        #p_ansi_len = len(paragraph) - len(strip_ansi(paragraph))
        #Line availability = width (default: 78) - length of pre_text
        line_available_chars = width - indent
        line_list = []
        line_text = ""
            
        words = re.findall(r"((?:\S+\s*)|(?:^\s+))", paragraph)
        for word in words:
             #available characters = word length + ansi characters
            line_available_chars += len(word) - len(strip_ansi(word))

            #if word can fit, put it in
            if len(word) <= line_available_chars:
                line_text += word
                line_available_chars -= len(word)
            #if word is longer than a whole line...
            elif len(word) > width - indent:
                #line_available_chars
                #Consider ansi codes attached to their subsequent character.
                ansi_character_list = re.findall(r"((?:\|[bBcCgGmMrRwWxXyY])|\|\d{3}|(?:.))", word)
                for character in ansi_character_list:
                    #If there's room to smoosh in the blob on this line, do so.
                    if line_available_chars >= 1: 
                        line_text += character
                        #line_available_chars -= len(strip_ansi(character))
                        if not character in ansi_character_list:
                            line_available_chars -= len(character)
                            #return line_available_chars
                        else:
                            line_available_chars -= len(strip_ansi(character))
                    #If not, start using hyphens and carry over.
                    else:
                        line_text += "-"
                        line_list.append(line_text)
                        line_text = character
                        if character in ansi_character_list:
                            line_available_chars = width - indent - 1
                        else:
                            line_available_chars = width - indent

            #if word cannot fit, begin a new line
            else:
                line_list.append(line_text)
                line_text = word
                line_available_chars = width - indent - len(line_text)#(2 * len(word) - len(strip_ansi(word)))
         
        line_list.append(line_text)
        first_line = True
        final_text = ""
        for line in line_list:
            if (len(line) - len(strip_ansi(line)) > 0):
                spaces = len(line) - len(strip_ansi(line))
            else:
                spaces = 0

            line_text = ""

            if first_line:
                line_text = justify(line, width = width+spaces,  indent = 0) #align = align,)
                first_line = False
            else:
                line_text = justify(line, width = width+spaces, indent = indent) #align = align, indent = indent)

            final_text += line_text + "\n"
    return pre_text + final_text[:-1] + "|n"

def justify(text, width, indent): #align,):
    return " " * indent + text

#    if align == "l":
#        return " "*indent + text
#    elif align == "c":
#        return " "*((width/2)-(len(text)/2)) + text

#    return text