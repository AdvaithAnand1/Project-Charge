def getLine(filepath, number):
    # generalized function to get a singular line form the file
    with open(filepath, 'r') as f:
        text = f.readlines()
    return text[number-1].rstrip('\n')
def getActiveTime():
    # call the getline function and return the tuple
    return (float(getLine("data", 2)), float(getLine("data", 4)))
def getInactiveTime():
    # return the flipped tuple of the prebious
    return (float(getLine("data", 4)), float(getLine("data", 2)))
def getDefaultLimit():
    # get the stored configuration
    return float(getLine("data", 6))
def store(filepath, linnum, string):
    # open the file and read all of the lines
    with open(filepath, 'r') as f:
        text = f.readlines()
    
    # make the necessary modifictions to the intended line
    if linnum < 1 or linnum > len(text):
        raise ValueError("Line number out of range.")
    if not string.endswith('\n'):
        string += '\n'
    
    # reinsert the information back into the document
    text[linnum-1] = string
    with open(filepath, 'w') as f:
        f.writelines(text)
