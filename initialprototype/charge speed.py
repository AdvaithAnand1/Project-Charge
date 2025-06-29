import time
def charge():
  print("This program will analyze the speed in which your device charges to make it possible to maintain charge.")
  import psutil
  def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)
  battery = psutil.sensors_battery()
  print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))