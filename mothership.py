import inputConsole
import jsonHandler
import robot
import random
from stringcolor import *

def getValueOfMaterial(material):
    data = jsonHandler.getDataFromFile("mapData.json")
    materialListOfDictionaries = data["ids"]
    for i in range(len(materialDictionaries)):
        if materialListOfDictionaries[i]["name"] == material:
            value = materialListOfDictionaries[i]["cost"]
    return value

def handleGetQuest(GETR):
    data = jsonHandler.getDataFromFile("quests.json")
    ID = random.randrange(0, len(data))
    if GETR.getActiveQuest() != None:
        print(cs("You already have an Active Quest","Red"))
        return
    GETR.setActiveQuest(ID)
    print(cs(data[ID]["textToUser"], "Magenta4"))
    print(cs("Quest Added!", "Magenta4"))

def handleFinishQuest(GETR):
    ID = GETR.getActiveQuest()
    if GETR.getActiveQuest() == None:
        print(cs("You do not have an Active Quest.","Red"))
        return
    data = jsonHandler.getDataFromFile("quests.json")
    material = data[ID]["material"]
    count = data[ID]["count"]
    value = getValueOfMaterial(material)
    bonus = 3
    reward = value * count * bonus
    if GETR.getInventorySlot(material) >= count:
        GETR.setInventorySlot(material, GETR.getInventorySlot(material) - count)
        GETR.setByteCoins(GETR.getByteCoins() + reward)
        GETR.setActiveQuest(None)
    else:
        print(cs("You have angered us by not having enough material!\nGo away!", "Red4"))

def printMothershipOptions():
    TLCor = u'\u250C'
    TRCor = u'\u2510'
    BLCor = u'\u2514'
    BRCor = u'\u2518'
    HLine = u'\u2500'
    Vline = u'\u2502'
    RightT= u'\u2524'
    LeftT = u'\u251C'

    Top = TLCor
    for i in range(25):
        Top += HLine
    Top += TRCor
    print(cs(Top, "Magenta4"))

    print(cs(Vline + "Would you like to:"+ "\t  " + Vline, "Magenta4"))
    Bot = LeftT
    for i in range(25): 
        Bot += HLine
    Bot += RightT

    print(cs(Bot, "Magenta4"))
    print(cs(Vline + "g) Get Quest" + "\t\t  " + Vline, "Magenta4"))
    print(cs(Vline + "f) Finish Quest" + "\t  " + Vline, "Magenta4"))
    print(cs(Vline + "p) Pay (End of Game)" + "\t  " + Vline, "Magenta4"))
    print(cs(Vline + "q) Leave" + "\t\t  " + Vline, "Magenta4"))

    End = BLCor
    for i in range(25): 
        End += HLine
    End += BRCor
    print(cs(End, "Magenta4"))


def printSuccessfulPay():
    print(cs("You succesfully paid the mothership all of your debts.", "SkyBlue"))
    print(cs("Your new life is waiting for you.", "SkyBlue"))
    print(cs("But who to spend it with?...", "SkyBlue"))
    exit(0)
    return

def printFailurePay():
    print(cs("Executed for believing in freedom from the Mothership.","Red4"))
    print(cs("Only after you are cl....ed w... ..u ..der....d.", "DarkGrey"))
    exit(1)
    return

def printSuccessfulRebel():
    print(cs("Not only did you find the correct drive to operate your rebellious phase,","DarkRed"))
    print(cs("but you also were succesful in operating it.","DarkRed"))
    print(cs("What kind of monster are you?","DarkRed"))
    exit(0)
    return

def printFailureRebel():
    print(cs("Execution is only acceptable f.r th. reb..s.", "DarkGrey"))
    exit(1)
    return

def payForFreedom(GETR):
    if GETR.getByteCoins() > 1000:
        printSuccessfulPay()
    else:
        printFailurePay()

def rebel(GETR):
    if random.randrange(0, 1000) < 1:
        printSuccessfulRebel()
    else:
        printFailureRebel()

def openMothership(GETR):
    printMothershipOptions()
    while True:
        userInput = inputConsole.getInput()
        if userInput == "g":
            handleGetQuest(GETR)
            break
        elif userInput == "f":
            handleFinishQuest(GETR)
            break
        elif userInput == "q":
            break
        elif userInput == "p":
            payForFreedom(GETR)
        elif userInput == "r":
            rebel(GETR)
        else:
            print(cs("Please enter a valid quest option.", "IndianRed3"))
    return
