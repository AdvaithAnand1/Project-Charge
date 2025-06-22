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
    history["SOURCE"] = history["SOURCE"].map(map).astype(float)
    history["CAPACITY REMAINING"] = history["CAPACITY REMAINING"].str[:-2].astype(float)
    dt_full = pd.to_datetime(history['START TIME'], errors = "coerce")
    history["DATE"] = dt_full.dt.day_name().ffill()
    history['TIME'] = pd.to_datetime(history['START TIME'], format = "mixed")
    map2 = {
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 7
    }
    history = history.drop("START TIME", axis = 1)
    history["DATE"] = history["DATE"].map(map2).astype(float)
    history["TIME"] = history["TIME"].dt.second + history["TIME"].dt.minute * 60 + history["TIME"].dt.hour * 3600
    return history