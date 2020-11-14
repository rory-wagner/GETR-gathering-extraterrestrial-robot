import inputConsole
import jsonHandler
import robot
import random

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
    if ID != None:
        print("You already have an Active Quest")
        return
    GETR.setActiveQuest(ID)
    print(data[ID]["textToUser"])
    print("Quest Added!")

def handleFinishQuest(GETR):
    ID = GETR.getActiveQuest()
    if ID == None:
        print("You do not have an Active Quest.")
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
        print("You have angered us by not having enough material!\nGo away!")

def printMothershipOptions():
    print("Would you like to:")
    print("g) Get Quest")
    print("f) Finish Quest")
    print("q) Leave")

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
        else:
            print("Please enter a valid quest option.")
    return
