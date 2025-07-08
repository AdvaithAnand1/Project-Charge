import extract, interact, network, regression, store
import time, math, numpy, torch
import subprocess, os, psutil
import torch
from datetime import datetime, date, time, timedelta

def nextActiveStart(start_hour: int) -> datetime:
    """
    Return the next datetime when the clock reaches start_hour:00.

    :param start_hour: Hour of day (0–23) when the active window starts.
    """
    now = datetime.now()
    # Build a datetime for today at start_hour:00
    today_target = datetime.combine(now.date(), time(start_hour, 0))
    # If that’s still in the future, use it; otherwise roll to tomorrow
    if today_target > now:
        return today_target
    else:
        return today_target + timedelta(days=1)

def is_active_time(time_obj, active):
   if(time_obj.tm_hour < active[0] or time_obj.tm_hour >= active[1]):
      print("returning false")
      return False
   print("returning true")
   return True
    # could work on implementing a more second and minute accurate approach

def calcChargeStart():
    model = network.load("network.pth")
    input_tensor = network.makeWeeklyInput(90)
    output = model.forward(input_tensor)
    max_vals, max_idxs = output.max(dim=1)
    preds = max_idxs.reshape((7,24))
    finalHour = store.getActiveTime()[0]
    finalDay = (nextActiveStart(int(store.getActiveTime()[0])).weekday() + 1) % 7
    startHour = datetime.now().hour
    startDay = (datetime.now().weekday() + 1) % 7
    hoursToCharge = extract.getChargeTime()
    i = int(finalHour)
    j = int(finalDay)
    count = 0
    while ((j > startDay or (j == startDay and i > startHour)) and count < hoursToCharge):
        if preds[j][i] == 1:
            count += 1
        i = (i - 1)
        if (i < 0):
            i = i % 24
            j = (j - 1) % 7
    print(f"day {j} of the week at {i}")
    if j==startDay:
        temp = datetime.combine(date.today(), time(i))
    else:
        temp = datetime.combine(date.today() + timedelta(1), time(i))
    return temp

chargingtime = calcChargeStart

if(not extract.checkExtracted()):
   extract.extractAll()

active_time = store.getActiveTime()
inactive_time = store.getInactiveTime()
defaultlimit = store.getDefaultLimit()

def main_loop():
   if(is_active_time(time.localtime(), store.getactivetime())):
      interact.setlimit(defaultlimit)
      charging = False
   elif (time.localtime() > chargingtime):
      interact.setlimit(100)
      charging = True
      if(greater than ending time): 
         charging = False
   else:
      # set charging flag to true and recalculate
      interact.setlimit(max(defaultlimit, psutil.sensors_battery().percent))
      chargingtime = calcChargeStart

while(True):
   main_loop()
   time.sleep(1)