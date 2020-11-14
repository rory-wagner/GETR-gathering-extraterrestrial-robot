import inputConsole
import jsonHandler
import robot
from stringcolor import *

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
        except ValueError:
            TLCor = u'\u250C'
            TRCor = u'\u2510'
            BLCor = u'\u2514'
            BRCor = u'\u2518'
            HLine = u'\u2500'
            Vline = u'\u2502'
            Top = TLCor
            for i in range(25):
                Top += HLine
            Top += TRCor    
            
            Bot = BLCor
            for i in range(25): 
                Bot += HLine
            Bot += BRCor    
        
            print(cs(Top, "Red"))
            print(cs(Vline + " Please give an integer. " + Vline, "Red"))
            print(cs(Bot, "Red"))

    return howMany

def handleBuy(GETR):

    while True:
        TLCor = u'\u250C'
        TRCor = u'\u2510'
        BLCor = u'\u2514'
        BRCor = u'\u2518'
        HLine = u'\u2500'
        Vline = u'\u2502'
        Top = TLCor
        for i in range(25):
            Top += HLine
        Top += TRCor
        
        Bot = BLCor
        for i in range(25): 
            Bot += HLine
        Bot += BRCor
    
        print(cs(Top, "Gold2"))
        print(cs(Vline + "  Current bytecoins: %s   " % GETR.getByteCoins() + Vline, "Gold2"))
        print(cs(Bot, "Gold2"))
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
                print(cs("===============================", "Red"))
                print(cs("Not enough bytecoins to spend", "Red"))
                print(cs("===============================", "Red"))

        elif userInput == "Q":
            break
        else:
            print(cs("===============================", "Red"))
            print(cs("Please enter full name of item", "Red"))
            print(cs("===============================", "Red"))

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
                print(cs("================", "Green3"))
                print(cs("Successful sell!", "Green3"))
                print(cs("================", "Green3"))
                break
            except:
                print(cs("==================================", "Red"))
                print(cs(("Not enough %s to sell" % userInput), "Red"))
                print(cs("==================================", "Red"))
        elif userInput == "Q":
            break
        else:
            print(cs("Please enter full name of item", "Red"))

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
