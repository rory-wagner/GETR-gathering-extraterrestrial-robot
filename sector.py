import gridMap
import jsonHandler
import random
import scenariosHandler

class Sector(gridMap.GridMap):
    def __init__(self, width, height, planet):
        gridMap.GridMap.__init__(self, width, height)
        self.planet = planet
        self.map[5][5] = 1
        self.generateMap(planet)

    def generateMap(self, planet):
        data = jsonHandler.getDataFromFile("planetData.json")
        concentrations = data["locationList"][planet]["concentration"]
        for i in range(self.width):
            for j in range(self.height):
                if (i != 5 or j != 5):
                    concentrationList = []
                    concentrationKeys = []
                    for key in concentrations:
                        if len(concentrationList) == 0:
                            concentrationList.append(concentrations[key])
                        else:
                            concentrationList.append(concentrationList[len(concentrationList) - 1] + concentrations[key])
                        concentrationKeys.append(key)
                    randomNum = random.randrange(0, 100)
                    for k in range(len(concentrationList)):
                        if randomNum <= concentrationList[k]:
                            self.map[i][j] = concentrationKeys[k]
                            break
    
    def reenterShip(self, GETR):
        #REEENTERING SHIP HERE****
        GETR.setX(self, 2)
        GETR.setY(self, 1)
        GETR.setOnPlanet(False)
        return "reentership"

    def interact(self, GETR):
        x = GETR.getX()
        y = GETR.getY()
        if x == 5 and y == 5:
            return self.reenterShip(GETR)
        else:
            ID = self.getCellID(x, y)
            data = jsonHandler.getDataFromFile("mapData.json")
            nameOfMaterial = data["ids"][ID]["name"]
            amountToAdd = random.randrange(0, 4)
            GETR.setInventorySlot(nameOfMaterial, amountToAdd)
            print(str(amountToAdd) + " " + nameOfMaterial + "s obtained!")
            #empty out the cell:
            self.setCellID(x, y, 0)
        return

    def checkAndDoRandomScenario(self, GETR):
        #check if place can be scenario available, then do it
        x = GETR.getX()
        y = GETR.getY()
        if self.getCellID(x, y) == 0:
            if random.randrange(0,100) < 100:
                scenariosHandler.performRandomScenario(GETR, self)
