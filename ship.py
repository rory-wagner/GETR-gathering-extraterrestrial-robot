import gridMap
import jsonHandler
import robot
import inputConsole
import shop

def printAllLocations(listOfStrings):
    for i in range(len(listOfStrings)):
        print(("%s) " % i) + listOfStrings[i])

def makeValidList(allPlanets):
    finalList = []
    for i in range(len(allPlanets["allLocations"])):
        finalList.append(i)
    return finalList

def getUserInput(validList):
    while True:
        userInput = inputConsole.getInput()
        try:
            userInput = int(userInput)
            if userInput in validList:
                return userInput
            else:
                raise Exception
        except:
            print("Please use a valid integer for location")

class Ship(gridMap.GridMap):
    def __init__(self):
        #width and height of ship:
        gridMap.GridMap.__init__(self, 3, 4)
        self.cargo = self.createCargo()
        self.maxCargo = 100
        self.rooms = [
            #x, y, roomID
            (1,0,2),
            (0,3,3),
            (2,3,4),
            (0,0,5),
            (2,1,14),
            (1,3,15)
        ]
        self.generate()

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
        allItemsAndWorth = jsonHandler.getDataFromFile("mapData.json")
        ourNewInventory = {}
        for i in allItemsAndWorth["materialIndexes"]:
            ourNewInventory[allItemsAndWorth["ids"][i]["name"]] = 0
        return ourNewInventory

    def generate(self):
        for i in range(self.width):
            for j in range(self.height):
                self.visitedMap[i][j] = True
                self.map[i][j] = 0
        for x, y, roomID in self.rooms:
            self.map[x][y] = roomID
        return

    def interact(self, GETR):
        for x, y, roomID in self.rooms:
            if GETR.getX() == x and GETR.getY() == y:
                if roomID == 2:
                    return self.ControlSeatInteract(GETR)
                elif roomID == 3:
                    return self.GeneratorInteract(GETR)
                elif roomID == 4:
                    return self.PropellantTankInteract(GETR)
                elif roomID == 5:
                    return self.CargoInteract(GETR)
                elif roomID == 14:
                    return self.ExitInteract(GETR)
                elif roomID == 15:
                    return self.EngineInteract(GETR)

    def ControlSeatInteract(self, GETR):
        #select new planet and tell main to call
        allPlanets = jsonHandler.getDataFromFile("planetData.json")
        allLocations = allPlanets["allLocations"]
        printAllLocations(allLocations)

        validList = makeValidList(allPlanets)

        userInput = getUserInput(validList)
        userSelectedPlace = allPlanets["allLocations"][userInput]
        if userSelectedPlace == "Shop":
            shop.openShop(GETR)
        return userSelectedPlace

    def GeneratorInteract(self, GETR):
        print("Generator is running well.")
        return
    
    def PropellantTankInteract(self, GETR):
        #check if they have and want to use a propellant tank to fuel the ship
        return

    def CargoInteract(self, GETR):
        #Let them choose to place things in or take things out of cargo
        # then act accordingly
        return

    def ExitInteract(self, GETR):
        print("Exiting ship")
        return "Exit"

    def EngineInteract(self, GETR):
        print("Engine is running well.")
        return

    def setVisited(self, x, y):
        #Dummy method, nothing to see here.
        return


