import pandas as pd
def getactivetime():

def getinactivetime():

def check_extracted():
    # if last extracted is one week or more before or has no been extracted before
    # call extract all
def extract_all():
    # extract all of the important information from the battery report
    # this includes the 
    getactivetime()
    getinactivetime()
    network.save(network.trainnetwork(gettable(r"C:\Windows\System32\battery-report.html")))
def gettable(file_path):
    history = pd.read_html(file_path)[2]
    history = history[history['STATE'] != 'Suspended'].drop(["CAPACITY REMAINING.1", "STATE"], axis = 1)
    map = {
        "AC": 1,
        "Battery": 0
    }
    history["SOURCE"] = history["SOURCE"].map(map)
    history["CAPACITY REMAINING"] = history["CAPACITY REMAINING"].str[:-2].astype(float)
    dt_full = pd.to_datetime(history['START TIME'], errors = "coerce")
    history["DATE"] = dt_full.dt.date.ffill()
    history['TIME'] = pd.to_datetime(history['START TIME'], format = "mixed").dt.time
    history = history.drop("START TIME", axis = 1)
    return history