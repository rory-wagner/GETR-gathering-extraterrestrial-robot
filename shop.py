import inputConsole
import jsonHandler
import robot

def getShop():
    allMapData = jsonHandler.getDataFromFile("mapData.json")
    DictOfNameAndCost = {}
    for i in allMapData["materialIndexes"]:
        DictOfNameAndCost[allMapData["ids"][i]["name"]] = allMapData["ids"][i]["cost"]
    return DictOfNameAndCost

def displayAndGetShop(GETR):
    DictOfNameAndCost = getShop()
    for key in DictOfNameAndCost:
        print("%s) " % key + str(DictOfNameAndCost[key]))
    return DictOfNameAndCost

def askHowMany():
    howMany = 0
    while True:
        print("How many to exchange?")
        try: 
            howMany = int(inputConsole.getNormalInput())
            break
        except:
            ("Please give an integer.")
    return howMany

def handleBuy(GETR):

    while True:
        print("Current bytecoins: %s" % GETR.getByteCoins())
        shopItemNamesAndCost = displayAndGetShop(GETR)
        #printQuit option:
        print("q) Quit")
        userInput = inputConsole.getInput().title()
        if userInput in shopItemNamesAndCost:
            howMany = int(askHowMany())
            finalCost = howMany * shopItemNamesAndCost[userInput]
            try:
                GETR.setByteCoins(GETR.getByteCoins() - finalCost)
                GETR.setInventorySlot(userInput, GETR.getInventorySlot(userInput) + howMany)
                print("Successful buy!")
                break
            except:
                print("Not enough bytecoins to spend")
        elif userInput == "Q":
            break
        else:
            print("Please enter full name of item")

def printAndGetCurrentInventoryAndShop(GETR):
    shopItemNamesAndCost = getShop()
    inventory = GETR.getInventory()
    for key in inventory:
        print("%s) " % key + str(inventory[key]))
    return inventory, shopItemNamesAndCost

def handleSell(GETR):
    while True:
        currentInventoryNamesAndCount, shopItemNamesAndCost = printAndGetCurrentInventoryAndShop(GETR)
        #printQuit option:
        print("q) Quit")
        userInput = inputConsole.getInput().title()
        if userInput in shopItemNamesAndCost:
            howMany = int(askHowMany())
            finalCost = howMany * shopItemNamesAndCost[userInput]
            try:
                GETR.setInventorySlot(userInput, GETR.getInventorySlot(userInput) - howMany)
                GETR.setByteCoins(GETR.getByteCoins() + finalCost)
                print("Successful sell!")
                break
            except:
                print("Not enough %s to sell" % userInput)
        elif userInput == "Q":
            break
        else:
            print("Please enter full name of item")

def printShopOptions():
    print("Would you like to:")
    print("b) Buy")
    print("s) Sell")
    print("q) Quit")

def openShop(GETR):
    printShopOptions()
    while True:
        userInput = inputConsole.getInput()
        if userInput == "b":
            handleBuy(GETR)
            printShopOptions()
        elif userInput == "s":
            handleSell(GETR)
            printShopOptions()
        elif userInput == "q":
            break
        else:
            print("Please enter a valid shopping option.")
            printShopOptions()
    return
