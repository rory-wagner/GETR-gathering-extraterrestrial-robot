import json
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
        return

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

    def setByteCoins(self, coins):
        if coins <= 0:
            self.byteCoins = 0
            raise BadInputException("Too little moneis given")
        else:
            self.byteCoins = coins

    def setX(self, specialMap, newX):
        if newX <= 0:
            self.x = 0
            raise BadInputException("Small x value given")
        elif newX > specialMap.getWidth()
            self.x = specialMap.getWidth()
            raise BadInputException("Large x value given")
        else:
            self.x = newX

    def setY(self, specialMap, newY):
        if newY <= 0:
            self.y = 0
            raise BadInputException("Small y value given")
        elif newY > specialMap.getWidth()
            self.y = specialMap.getWidth()
            raise BadInputException("Large y value given")
        else:
            self.y = newY

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
        self.inventory[item] = itemNum

    def fillInventory(self):
        allItemsAndWorth = jsonHandler.getDataFromFile("items.json")
        ourNewInventory = {}
        for key in allItemsAndWorth:
            ourNewInventory[key] = 0
        return ourNewInventory