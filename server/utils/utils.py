import re
import textwrap
from django.conf import settings
from evennia.utils.ansi import strip_ansi
from evennia.utils.utils import to_str, wrap

def grammarize(text, ending='.'):
    text = text.strip()
    if not text.endswith((".", "!", "?", ".'", "!'", "?'", '."', '!"', '?"')):
        text += ending

    if text[-2] == " ":
        text = text[:-2] + text[-1]
        
    return text

def wrap(text, text_width=None, screen_width=None, pre_text="", indent=0, align="l"):
    
    # Format Text
    text_width = text_width if text_width else settings.CLIENT_DEFAULT_WIDTH
    screen_width = screen_width if screen_width else settings.CLIENT_DEFAULT_WIDTH

    if screen_width is not None:
        text_lines = re.split(r"\n|\|/", text)
        final_text = pre_text
        first_line = True
        for x in text_lines:
            word_list = re.findall(r"((?:\S+\s*)|(?:^\s+))", x)
            line_list = []
            line_len = len(x) - len(strip_ansi(x))
            line_available_char = text_width - len(strip_ansi(pre_text))# + line_len
            line = ""
            for y in word_list:
                line_available_char = line_available_char + (len(y)-len(strip_ansi(y)))
                if (len(y) <= line_available_char):
                    line += y
                    line_available_char = line_available_char - len(y)
                else:
                    if (len(y) > text_width - len(strip_ansi(pre_text))):
                        line = ""
                        line_available_char = text_width - len(strip_ansi(pre_text))
                        character_list = re.findall(r"((?:\|[bBcCgGmMrRwWxXyY])|\|\d{3}|(?:.))", y)
                        for character in character_list:
                            if (len(character) <= line_available_char):
                                line += character
                                if not character in character_list:
                                    line_available_char = line_available_char - len(character)
                                    
                            else:
                                line_list.append(line)
                                line = character
                                if character in character_list:
                                    line_available_char = text_width - len(strip_ansi(pre_text))
                                else:
                                    line_available_char = text_width - len(strip_ansi(pre_text)) - len(character)
                    else:
                        line_list.append(line)
                        line = y
                        line_available_char = text_width - len(strip_ansi(pre_text)) - len(y) + (len(y)-len(strip_ansi(y)))
            line_list.append(line)
            for y in line_list:
                if ((len(y) - len(strip_ansi(y))) > 0):
                    spaces = len(y) - len(strip_ansi(y))
                else:
                    spaces = 0
                        
                line_text = ""
        
                if first_line:
                    final_text = justify(final_text, width=screen_width+spaces, align=align, indent=indent)
                    line_text = justify(y, width=screen_width+spaces, align=align)
                else:
                    line_text = justify(y, width=screen_width+spaces, align=align, indent=len(strip_ansi(pre_text))+indent)

                final_text += line_text+"|/"
                first_line = False
    final_text = final_text[:-2]
    return final_text + "|n"


def justify(text, width=settings.CLIENT_DEFAULT_WIDTH, align="l", indent=0):
    
    if align == "l":
        return "|n" + " "*indent + text
    elif align == "c":
        return " "*((width/2)-(len(text)/2)) + text

    return text


"""
def wrap(text, width = None, pre_text = "", indent = 0):
    
    #Safely wrap text to a certain number of characters.

    #Args:
    #    text (str): The text to wrap.
    #    width (int, optional): The number of characters to wrap to.
    #    indent (int): How much to indent each line (with whitespace).

    #Returns:
    #    text (str): Properly wrapped text.

    #Note: Could probably be optimized with a while loop.

    
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
"""