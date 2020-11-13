import gridMap
import jsonHandler

class Ship(gridMap.GridMap):
    def __init__(self, width, height):
        self.cargo = self.createCargo()
        self.maxCargo = 100
        gridMap.GridMap.__init__(self, width, height)

    def getMaxCargo(self):
        return self.maxCargo

    def setMaxCargo(self, newMax):
        oldMax = self.maxCargo
        if newMax <= 0:
            self.maxCargo = 0
            raise BadInputException("Small max charge given")
        else:
            self.maxCargo = newMax

        if self.maxCargo <= oldMax:
            if self.getCurrCharge() < self.maxCargo:
                self.setCurrCharge(newMax)

    def getCargo(self):
        return self.cargo

    def setCargoItem(self, itemString, value):
        self.cargo[itemString] = value

    def createCargo(self):
        allItemsAndWorth = jsonHandler.getDataFromFile("items.json")
        ourNewInventory = {}
        for key in allItemsAndWorth:
            ourNewInventory[key] = 0
        return ourNewInventory

    def generate(self):
        for i in range(self.width):
            for j in range(self.height):
                self.map[i][j]


testShip = Ship(5, 5)

