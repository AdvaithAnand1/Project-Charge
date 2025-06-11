#Opens the file in the folder "Stored Data", 'settings.txt', and reads it.
with open('Stored Data/settings.txt', 'r') as f:
	data = f.readlines()
#Imports
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
import time
def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False
def integerInput():
  try:
    newPercent = int(input("\nPlease enter the new INTEGER that you want to set the percent to: "))
    if 1 <= newPercent and newPercent <= 100:
      return(newPercent)
    else:
      print("The value has to be in between 1 to 100.")
      integerInput()
  except ValueError:
    print("Please try again with a valid INTEGER.")
    clearConsole()
    integerInput()
def intConvert(wrongNumber):
  tempList = list(wrongNumber)
  counter = 0
  for i in tempList:
    counter = counter + 1
  wrongNumber = ""
  x = 0
  while x < counter - 1:
    wrongNumber += tempList[x]
    x += 1
  return(wrongNumber)
  #Allows user to interact with the program and switch through various options in the settings.
def navSettings(choice):
  if choice == "Debug":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Debug")
    debugSettings()
  elif choice == "Mode":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Mode")
    modeSettings()
  elif choice == "Daytime Settings":
    clearConsole
    if data[1] == "true\n":
      print("Debug - Daytime Settings")
    daytimeSettings()
  elif choice == "Nighttime Settings":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Nighttime Settings")
    nighttimeSettings()
  elif choice == "exit":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Returning To Main")
    import main
    main.main()
  else:
    clearConsole()
    print("Remember That Your Input is Case Sensitive. Try to reenter your choice.")
    settings()

def settings():
  print("Entered Settings")
  if data[1] == "true":
	  print("Debug - Settings Called")
  print("Please Enter Which Part of The Settings You Want To View. The options are Debug, Mode, Daytime Settings, Nighttime Settings, and exit.")
  navChoice = str(input("Enter Here: "))
  navSettings(navChoice)
#Allowing the user to see the running code.
def debugSettings():
  print("Welcome to debug section. This option allows the user to know what code is currently running. This is mainly implemented to support developers while making this program.")
  if data[1] == "true\n":
    print("The debug fuction is currently enabled.")
  if data[1] == "false\n":
    print("The debug fuction is currently disabled.")
  debugChoice = input("Please choose if you want to 'enable', 'disable', or 'exit': ")
  if debugChoice == "enable":
    data[1] = "true\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    print("Debug - Debug Enabled")
    settings()
  elif debugChoice == "disable":
    data[1] = "false\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    settings()
  elif debugChoice == "exit":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Exitting Debug Settings")
    settings()
  else:
    clearConsole()
    print("Remember That Your Input is Case Sensitive. Try to reenter your choice.")
    debugSettings()
#An option made to have the program running while asleep.
def modeSettings():
  print("Welcome to mode section. This option allows the user to choose the program to run at the time they sleep. Most people will enter night for this option as not a lot of people sleep in the day and work in the night. Remember that mode is TIME when you SLEEP.")
  if data[3] == "night\n":
    print("The mode is currently set to sleeping in the night.")
  if data[3] == "day\n":
    print("The mode is currently set to sleeping in the day.")
  modeChoice = input("Please choose if you want to set it to 'night', 'day', or 'exit': ")
  if modeChoice == "night":
    data[3] = "night\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Mode Set To Night")
    settings()
  elif modeChoice == "day":
    data[3] = "day\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Mode Set To Day")
    settings()
  elif modeChoice == "exit":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Exitting Mode Settings")
    settings()
  else:
    clearConsole()
    print("Remember That Your Input is Case Sensitive. Try to reenter your choice.")
    modeSettings()
#Allows the user to enable or disable this setting. When enabled, the user will be prompted to type in a percentage at which their device will stay at.
def daytimeSettings():
  print("Welcome to the daytime settings. This has two subsections, battery percentage and enable or disable. First you will get the option to enable or disable. After you choose that, you can type in a percentage that your device should be maintained at.")
  if data[5] == "on\n":
    print("This program will currently run in the day.")
  if data[5] == "off\n":
    print("The mode is currently set to sleeping in the day.")
  dayChoice = input("Please choose if you want to set it to 'on', 'off', or 'exit': ")
  if dayChoice == "on":
    data[5] = "on\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Daytime Settings Enabled")
  elif dayChoice == "off":
    data[5] = "off\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Daytime Settings Disabled")
    settings()
  elif dayChoice == "exit":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Exitting Daytime Settings")
    settings()
  else:
    clearConsole()
    print("Remember That Your Input is Case Sensitive. Try to reenter your choice.")
    daytimeSettings()
  print("Now you will get the chance to change the percentage this program will use when maintaining battery life. The suggested for daytime is 75%. Only enter an INTEGER between 1 to 100.")
  try:
    print("Your current percentage is " + intConvert((data[7])) + "%.")
  except ValueError:
    print("An error occurred because the stored values were editted incorrectly by user. Please go and undo changes that were made in the text file.")
  newPercent = integerInput()
  data[7] = str(newPercent) + "\n"
  with open('Stored Data/settings.txt', 'w') as f:
    f.writelines(data)
  clearConsole()
  if data[1] == "true\n":
    print("Debug - Percentage Changed")
  settings()
#Another interface allowing the user to select options during use of their device in the night.
def nighttimeSettings():
  print("Welcome to the nighttime settings. This has four subsections, battery percentage, enable or disable, auto or manual, and time. First you will get the option to enable or disable. After you choose that, you can type in a percentage that your device should be maintained at. third, there will be an option to use automatic time finding or manual. Then it will give an option to set the time when it will reach 100%.")
  if data[9] == "on\n":
    print("This program will currently run in the night.")
  if data[9] == "off\n":
    print("This program will not run in the night.")
  nightChoice = input("Please choose if you want to set it to 'on', 'off', or 'exit': ")
  if nightChoice == "on":
    data[9] = "on\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Nighttime Settings Enabled")
  elif nightChoice == "off":
    data[9] = "off\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Nighttime Settings Disabled")
    settings()
  elif nightChoice == "exit":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Exitting Nightime Settings")
    settings()
  else:
    clearConsole()
    print("Remember That Your Input is Case Sensitive. Try to reenter your choice.")
    nighttimeSettings()
  print("Now you will get the chance to change the percentage this program will use when maintaining battery life. The suggested for daytime is 50%. Only enter an INTEGER between 1 to 100.")
  try:
    print("Your current percentage is " + intConvert((data[11])) + "%.")
  except ValueError:
    print("An error occurred because the stored values were editted incorrectly by user. Please go and undo changes that were made in the text file.")
  newPercent = integerInput()
  data[11] = str(newPercent) + "\n"
  with open('Stored Data/settings.txt', 'w') as f:
    f.writelines(data)
  clearConsole()
  if data[1] == "true\n":
    print("Debug - Percentage Changed")
  print("The current option is set to " + data[13])
  nightChoice = input("Please choose if you want to set it to 'auto', 'manual', or 'exit': ")
  if nightChoice == "auto":
    data[13] = "auto\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Nighttime Settings Auto")
    settings()
  elif nightChoice == "manual":
    data[13] = "manual\n"
    with open('Stored Data/settings.txt', 'w') as f:
      f.writelines(data)
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Nighttime Settings Manual")
  elif nightChoice == "exit":
    clearConsole()
    if data[1] == "true\n":
      print("Debug - Exitting Nightime Settings")
    settings()
  else:
    clearConsole()
    print("Remember That Your Input is Case Sensitive. Try to reenter your choice.")
    nighttimeSettings()
  print("Now you will enter the time at which you want your phone to reach 100%. You must enter the time like 09:45. It must have 2 digits in both parts.")
  timeTo100 = input("Enter here: ")
  if isTimeFormat(timeTo100) != True:
    clearConsole()
    print("Error. Remember to follow the correct format.")
    nighttimeSettings()
  data[15] = timeTo100 + "\n"
  with open('Stored Data/settings.txt', 'w') as f:
    f.writelines(data)
  clearConsole()
  if data[1] == "true\n":
    print("Debug - New Time Saved")
  settings()