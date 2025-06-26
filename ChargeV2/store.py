def getline(filepath, number):
    with open(filepath, 'r') as f:
        text = f.readlines()
    return text[number-1].rstrip('\n')
def getactivetime():
    return (float(getline("data", 2)), float(getline("data", 4)))
def getinactivetime():
    return (float(getline("data", 4)), float(getline("data", 2)))
def getdefaultlimit():
    return float(getline("data", 6))
def getlastdate():
    return getline("data", 8)
def store(filepath, linnum, string):
    with open(filepath, 'r') as f:
        text = f.readlines()
    
    if linnum < 1 or linnum > len(text):
        raise ValueError("Line number out of range.")
    if not string.endswith('\n'):
        string += '\n'
    
    text[linnum] = string
    with open(filepath, 'w') as f:
        f.writelines(text)
