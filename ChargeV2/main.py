import extract, interact, network, regression, store
import math, numpy, torch
import subprocess, os, psutil
import torch
import time as timemodule
from datetime import datetime, date, time, timedelta

import os
print(os.getcwd())
def nextActiveStart(start_hour: int) -> datetime:
    # get the current date
    now = datetime.now()
    # create an object with today's date at the ideal time
    today_target = datetime.combine(now.date(), time(start_hour, 0))
    # if we are past the time, shift it to the next day
    if today_target > now:
        return today_target
    else:
        return today_target + timedelta(days=1)

def is_active_time(time_obj: time, active: (float, float)):
    # check whether the passed time is within the tuple active time
    if(time_obj.tm_hour < active[0] or time_obj.tm_hour >= active[1]):
      print("returning false")
      return False
    print("returning true")
    return True

def calcChargeStart():
    # load in the previously saved neural network
    model = network.load("network.pth")

    # create a prediction tensor that will hold a boolean value stating whether the device would be charging at that specific moment
    input_tensor = network.makeWeeklyInput(90)
    output = model.forward(input_tensor)
    max_vals, max_idxs = output.max(dim=1)
    preds = max_idxs.reshape((7,24))

    # estalish the boundary variables for the loop
    finalHour = store.getActiveTime()[0]
    finalDay = (nextActiveStart(int(store.getActiveTime()[0])).weekday() + 1) % 7
    startHour = datetime.now().hour
    startDay = (datetime.now().weekday() + 1) % 7

    # retrieve the amount of time we need to charge for to reach the battery capacity
    hoursToCharge = extract.getChargeTime()
    
    # make clones of the variables for looping purposes
    i = int(finalHour)
    j = int(finalDay)
    count = 0

    # starting from the time at which we need to wake up the device, back track and find the latest possible charging time
    while ((j > startDay or (j == startDay and i > startHour)) and count < hoursToCharge):
        if preds[j][i] == 1:
            count += 1
        i = (i - 1)
        if (i < 0):
            i = i % 24
            j = (j - 1) % 7
    # for simplicity sake take advantage of the only two possible dates being the current day or next day
    if j==startDay:
        temp = datetime.combine(date.today(), time(i))
    else:
        temp = datetime.combine(date.today() + timedelta(days=1), time(i))
    return temp

# check if all of the necessary information is already extracted from their respective data sources
# if not call the extraction process
if(not extract.checkExtracted()):
   extract.extractAll()

# get the initial calculation of the charge starting time
chargingtime = calcChargeStart()

# retrieve some of the necessary information from the stored files
active_time = store.getActiveTime()
inactive_time = store.getInactiveTime()
defaultlimit = store.getDefaultLimit()

def main_loop():
    global chargingtime
    # if we are in the active time, it means that we can set it to default and turn off charging
    if(is_active_time(timemodule.localtime(), store.getActiveTime())):
        print("active")
        interact.setlimit(defaultlimit)
        charging = False
    # if the current time is past the calculated charging time, set the limit to 100
    elif (datetime.now() > chargingtime):
        print("charging")
        interact.setlimit(100)
    # else it means that we are waiting for the charging time to come so repeat the recalculation every second
    else:
        print("inactive waiting")
        interact.setlimit(max(defaultlimit, psutil.sensors_battery().percent))
        chargingtime = calcChargeStart()
        print(f"calculated: {chargingtime}")
while(True):
   main_loop()
   timemodule.sleep(5)