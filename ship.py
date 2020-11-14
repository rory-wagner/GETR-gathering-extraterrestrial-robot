import gridMap
import jsonHandler
import robot
import inputConsole
import shop
import mothership
from stringcolor import *

def printAllLocations(listOfStrings):
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
    
    Bot = LeftT
    for i in range(25): 
        Bot += HLine
    Bot += RightT

    End = BLCor
    for i in range(25): 
        End += HLine
    End += BRCor

    print(cs(Top, "Turquoise2"))
    print(cs(Vline + "    Where to Skipper?    " + Vline, "Turquoise2"))
    print(cs(Bot, "Turquoise2"))

    for i in range(len(listOfStrings)):
        mystring = ( " %s) " % i) + listOfStrings[i]
        chars = len(mystring)
        bigskip = ""
        for i in range(25 - chars):
            bigskip += " "
        print(cs((Vline + mystring + bigskip + Vline), "Turquoise2"))
    print(cs(End, "Turquoise2"))

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
            TLCor = u'\u250C'
            TRCor = u'\u2510'
            BLCor = u'\u2514'
            BRCor = u'\u2518'
            HLine = u'\u2500'
            Vline = u'\u2502'

            Top = TLCor
            for i in range(33):
                Top += HLine
            Top += TRCor

            print(cs(Top, "Turquoise2"))
            print(cs(Vline + "Sorry Cap'n hav'n heard of there." + Vline, "Turquoise2"))
            End = BLCor
            for i in range(33): 
                End += HLine
            End += BRCor

            print(cs(End, "Turquoise2"))

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
        elif userSelectedPlace == "Mothership":
            mothership.openMothership(GETR)
        return userSelectedPlace

    def GeneratorInteract(self, GETR):
        print("Generator is running well.")
        return
    
    def PropellantTankInteract(self, GETR):
        print("Tank is fueled up.")
        return

    def CargoInteract(self, GETR):
        #Let them choose to place things in or take things out of cargo
        # then act accordingly
        return

    def ExitInteract(self, GETR):
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

        print(cs(Top, "Violet"))

        monologue = [" Exiting ship...", " I'll miss you!", " Be safe!", 
            " Make good choices!", " Remember who you are!",  
            " Oh.They grow up so fast."
        ]
        for text in monologue:
            textline = Vline + text
            textnum = len(text)
            for i in range(25 - textnum):
                textline += " "
            textline += Vline
            print(cs(textline, "Violet"))

        End = BLCor
        for i in range(25): 
            End += HLine
        End += BRCor
        print(cs(End, "Violet"))

        return "Exit"

    def EngineInteract(self, GETR):
        print("Engine is running well.")
        return

    def setVisited(self, x, y):
        #Dummy method, nothing to see here.
        return


