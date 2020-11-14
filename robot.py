import jsonHandler

class BadInputException(Exception):
    pass

class RanOutOfBattery(Exception):
    pass

class Robot:
    def __init__(self):
        self.byteCoins = 0
        self.x = 0
        self.y = 0
        self.onPlanet = False
        self.currCharge = 50
        self.maxCharge = 50
        self.inventory = self.fillInventory()
        self.ActiveQuest = None
        self.confusedCounter = 0
        return

    def incConfusedCounter(self):
        self.confusedCounter += 1

    def getConfusedCounter(self):
        return self.confusedCounter

    def setActiveQuest(self, num):
        self.ActiveQuest = num

    def getActiveQuest(self):
        return self.ActiveQuest

    def getByteCoins(self):
        return self.byteCoins

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getOnPlanet(self):
        return self.onPlanet

    def getCurrCharge(self):
        return self.currCharge

    def getMaxCharge(self):
        return self.maxCharge

    def getInventory(self):
        return self.inventory

    def getInventorySlot(self, key):
        return self.inventory[key.title()]

    def setByteCoins(self, coins):
        if coins < 0:
            # self.byteCoins = 0
            raise BadInputException("Too little moneis given")
        else:
            self.byteCoins = coins

    def setX(self, currentMap, newX):
        if newX < 0:
            self.x = 0
            currentMap.setVisited(self.getX(), self.getY())
            raise BadInputException("Small x value given")  
        elif newX == currentMap.getWidth():
            self.x = currentMap.getWidth() - 1
            currentMap.setVisited(self.getX(), self.getY())
            raise BadInputException("Large x value given")
        else:
            self.x = newX
            currentMap.setVisited(self.getX(), self.getY())
            currentMap.checkAndDoRandomScenario(self)


    def setY(self, currentMap, newY):
        if newY < 0:
            self.y = 0
            currentMap.setVisited(self.getX(), self.getY())
            raise BadInputException("Small y value given")
        elif newY == currentMap.getHeight():
            self.y = currentMap.getHeight() - 1
            currentMap.setVisited(self.getX(), self.getY())
            raise BadInputException("Large y value given")
        else:
            self.y = newY
            currentMap.setVisited(self.getX(), self.getY())
            currentMap.checkAndDoRandomScenario(self)

    def setOnPlanet(self, value):
        self.onPlanet = value

    def setCurrCharge(self, newC):
        if newC <= 0:
            self.currCharge = 0
            raise RanOutOfBattery("Too little battery, must replace battery or power down")
        elif newC > self.getMaxCharge():
            self.currCharge = self.getMaxCharge()
        else:
            self.currCharge = newC

    def setMaxCharge(self, newMax):
        oldMax = self.maxCharge
        if newMax <= 0:
            self.maxCharge = 0
            raise BadInputException("Small max charge given")
        else:
            self.maxCharge = newMax

        if self.maxCharge <= oldMax:
            if self.getCurrCharge() < self.maxCharge:
                self.setCurrCharge(newMax)


    def setInventorySlot(self, item, itemNum):
        #might need more error checking here if we want a maximum on the inventory.
        #also check if given bad item
        if itemNum < 0:
            raise BadInputException("Trying to sell too much")
        else:
            self.inventory[item] = itemNum

    def fillInventory(self):
        allItemsAndWorth = jsonHandler.getDataFromFile("mapData.json")
        ourNewInventory = {}
        for i in allItemsAndWorth["materialIndexes"]:
            ourNewInventory[allItemsAndWorth["ids"][i]["name"]] = 0
        return ourNewInventory
