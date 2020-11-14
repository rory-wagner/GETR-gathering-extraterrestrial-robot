import gridMap
import jsonHandler
import robot
import inputConsole

def printAllLocations(listOfStrings):
    for i in range(len(listOfStrings)):
        print(("%s) " % i) + listOfStrings[i])

def makeValidList(allPlanets):
    finalList = []
    for i in range(len(allPlanets["allLocations"])):
        finalList.append(i)
    return finalList

def getUserInput():
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


#callback Functions:

def emptyFunction():
    return


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
        allItemsAndWorth = jsonHandler.getDataFromFile("items.json")
        ourNewInventory = {}
        for key in allItemsAndWorth:
            ourNewInventory[key] = 0
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
                    self.ControlSeatInteract(GETR)
                elif roomID == 3:
                    self.GeneratorInteract(GETR)
                elif roomID == 4:
                    self.PropellantTankInteract(GETR)
                elif roomID == 5:
                    self.CargoInteract(GETR)
                elif roomID == 14:
                    self.ExitInteract(GETR)
                elif roomID == 15:
                    self.EngineInteract(GETR)

    def ControlSeatInteract(self, GETR):
        #select new planet and tell main to call
        allPlanets = jsonHandler.getDataFromFile("planetData.json")
        allLocations = allPlanets["allLocations"]
        printAllLocations(allLocations)

        validList = makeValidList(allPlanets)

        userInput = getUserInput(validList)
        userSelectedPlace = allPlanets["allLocations"][userInput]
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
        return "Exit"

    def EngineInteract(self, GETR):
        print("Engine is running well.")
        return

