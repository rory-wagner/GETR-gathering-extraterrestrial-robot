import inputConsole
import jsonHandler

def displayAndGetShop(GETR):
    allMapData = jsonHandler.getDataFromFile("mapData.json")
    DictOfNameAndCost = {}
    for i in allMapData["materialIndexes"]:
        DictOfNameAndCost[allMapData["ids"][i]["name"]] = allMapData["ids"][i]["cost"]
    for key in DictOfNameAndCost:
        print("%s) " % key + str(DictOfNameAndCost[key]))
    return DictOfNameAndCost


def handleBuy(GETR):
    print("Current bytecoins: %s" % GETR.getByteCoins())
    shopItemNamesAndCost = displayAndGetShop(GETR)


def openShop(GETR):
    print("Would you like to:")
    print("b) Buy")
    print("s) Sell")
    print("q) Quit")
    while True:
        userInput = inputConsole.getInput()
        if userInput == "b":
            handleBuy(GETR)
            break
        elif userInput == "s":
            handleSell(GETR)
            break
        elif userInput == "q":
            break
        else:
            print("Please enter a valid option.")
    return
