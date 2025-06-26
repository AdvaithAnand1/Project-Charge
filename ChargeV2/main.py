import extract, interact, network, regression, store
import time, math, numpy, torch
import subprocess, os, psutil


def is_active_time(time_obj, active):
   if(time_obj.tm_hour < active[0] or time_obj.tm_hour >= active[1]):
      print("returning false")
      return False
   print("returning true")
   return True
    # could work on implementing a more second and minute accurate approach

if(not extract.check_extracted()):
   extract.extract_all()

active_time = store.getactivetime()
inactive_time = store.getinactivetime()
defaultlimit = store.getdefaultlimit()

def main_loop():
   if(is_active_time(time.localtime(), store.getactivetime())):
      interact.setlimit(defaultlimit)
      charging = False
   else if (time.localtime() > chargingtime):
      interact.setlimit(100)
      charging = True
      if(greater than ending time):
         charging = False
   else:
      # set charging flag to true and recalculate
      interact.setlimit(max(defaultlimit, psutil.sensors_battery().percent))
   
while(True):
   main_loop()
   time.sleep(1)