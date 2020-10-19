def grammarize(item):
    if item.name[0].lower() in ("a", "e", "i", "o", "u"):
        string = "an %s" % item.name
    else:
        string = "a %s" % item.name

    return string

def listarize(array):
    string = ""
    for item in array:
        if len(array) == 1:
            return f"{grammarize(item)}."
            
        #Items in a list of three or more need commas.
        if not array.index(item) == len(array) - 1:
            if not len(array) > 2:
                string += f"{grammarize(item)} "
            else:
                string += f"{grammarize(item)}, "
        #Final object is prefaced with an and.
        else:
            string += f"and {grammarize(item)}."

    return string