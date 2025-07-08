import pandas as pd
import datetime
import network, store
def extractActiveTime():
    print("activetimeextract")
    # implement a log analyzing algorithm to understand the times at which user turns on and usually turns off their machine
def getChargeTime():
    return 2

def checkExtracted():
    lastdate = datetime.date.fromisoformat(store.getLine("data", 8))
    date = datetime.date.today()
    if ((date - lastdate).days > 7):
        return False
    else:
        return True
def extractAll():
    extractActiveTime()
    network.save(r"C:\Windows\System32\battery-report.html")
    store.store("data", 7, str(datetime.date.today()))
def getTable(file_path):
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
    history["DATE"] /= 7
    history["TIME"] /= 24 * 3600
    history["CAPACITY REMAINING"] /= 100
    return history