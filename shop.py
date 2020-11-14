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
    TLCor = u'\u250C'
    TRCor = u'\u2510'
    BLCor = u'\u2514'
    BRCor = u'\u2518'
    HLine = u'\u2500'
    Vline = u'\u2502'
    RightT= u'\u2524'
    LeftT = u'\u251C'

    Top = TLCor
    for i in range(16):
        Top += HLine
    Top += TRCor
    print(cs(Top, "SeaGreen4"))

    print(cs(Vline+"      BUY      "+Vline, "SeaGreen4"))


    Bot = LeftT
    for i in range(16): 
        Bot += HLine
    Bot += RightT
    print(cs(Bot, "SeaGreen4"))

    DictOfNameAndCost = getShop()
    for key in DictOfNameAndCost:
        message =  "%s) " % key + str(DictOfNameAndCost[key])
        messagelen = len(message)
        for i in range(16 - messagelen):
            message += " "
        print(cs(Vline + message + Vline, "SeaGreen4"))

    End = BLCor
    for i in range(16): 
        End += HLine
    End += BRCor
    print(cs(End, "SeaGreen4"))

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
        print(cs("q) Quit", "IndianRed2"))
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
    TLCor = u'\u250C'
    TRCor = u'\u2510'
    BLCor = u'\u2514'
    BRCor = u'\u2518'
    HLine = u'\u2500'
    Vline = u'\u2502'
    RightT= u'\u2524'
    LeftT = u'\u251C'

    Top = TLCor
    for i in range(16):
        Top += HLine
    Top += TRCor
    print(cs(Top, "SeaGreen4"))

    print(cs(Vline+"      SELL      "+Vline, "SeaGreen4"))

    Bot = LeftT
    for i in range(16): 
        Bot += HLine
    Bot += RightT
    print(cs(Bot, "SeaGreen4"))

    shopItemNamesAndCost = getShop()
    inventory = GETR.getInventory()
    for key in inventory:
        message =  "%s) " % key + str(inventory[key])
        messagelen = len(message)
        for i in range(16 - messagelen):
            message += " "
        print(cs(Vline + message + Vline, "SeaGreen4"))

    End = BLCor
    for i in range(16): 
        End += HLine
    End += BRCor
    print(cs(End, "SeaGreen4"))

    return inventory, shopItemNamesAndCost



def handleSell(GETR):
    while True:
        currentInventoryNamesAndCount, shopItemNamesAndCost = printAndGetCurrentInventoryAndShop(GETR)
        #printQuit option:
        print(cs("q) Quit", "IndianRed2"))
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
    
    print(cs(Top, "SeaGreen4"))
    print(cs(Vline +"Would you like to:" + "       "+ Vline, "SeaGreen4"))
    Bot = LeftT
    for i in range(25): 
        Bot += HLine
    Bot += RightT

    print(cs(Bot, "SeaGreen4"))

    print(cs(Vline + "b) Buy" + "\t\t\t  " + Vline, "SeaGreen4"))
    print(cs(Vline + "s) Sell" + "\t\t  " + Vline, "SeaGreen4"))
    print(cs(Vline + "q) Quit" + "\t\t  " + Vline, "SeaGreen4"))


    End = BLCor
    for i in range(25): 
        End += HLine
    End += BRCor
    print(cs(End, "SeaGreen4"))



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
