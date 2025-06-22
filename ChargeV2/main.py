import extract, interact, network, regression, store
import time, math, numpy, torch
import subprocess, os, psutil


def is_active_time(time_obj, (i, j)):
    if(time_obj.tm_hour < i or time_obj.tm_hour >= j):
      return False
    return True
    # could work on implementing a more second and minute accurate approach

curr_time = time.localtime()

if(not extract.check_extracted()):
   extract.extract_all()


active_time = store.getactivetime()
inactive_time = store.getinactivetime()
defaultlimit = store.getdefaultlimit()

def main_loop(cur_time, active_time):
   if(is_active_time()):
      interact.setlimit(defaultlimit)
   else:
      interact.setlimit(max(defaultlimit, psutil.sensors_battery().percent))
   