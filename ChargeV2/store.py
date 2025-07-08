def getLine(filepath, number):
    with open(filepath, 'r') as f:
        text = f.readlines()
    return text[number-1].rstrip('\n')
def getActiveTime():
    return (float(getLine("data", 2)), float(getLine("data", 4)))
def getInactiveTime():
    return (float(getLine("data", 4)), float(getLine("data", 2)))
def getDefaultLimit():
    return float(getLine("data", 6))
def getLastData():
    return getLine("data", 8)
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
