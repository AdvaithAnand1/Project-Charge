import settings
y = False
print("Welcome to our new battery life saving application. This application will tell when to connect or disconnect your charger. Our future goal is to make supporting hardware.")
def nav(location):
  if location == "settings":
    y = True
    settings.settings()
  elif location == "charging":
    import charge_speed
    charge_speed.charge()
  elif location == "output":
    print("")
def mainFunction():
  print("There are 3 locations to go to, 'settings', 'charging', and 'output'. The settings is used to control all of the features of this program.")
  while y == False:
    loc = input("Please choose a location: ")
    nav(loc)
mainFunction()