def getline(filepath, number):
    with open(filepath, 'r') as f:
        text = f.readlines()
    return text[number-1].rstrip('\n')
def getactivetime():
    return (getline("data", 2), getline("data", 4))
def getinactivetime():
    return (getline("data", 4), getline("data", 2))
def getdefaultlimit():
    return getline("data", 6)