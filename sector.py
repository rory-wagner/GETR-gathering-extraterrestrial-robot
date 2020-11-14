import gridMap
import jsonHandler
import random

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
                if (i != 5 and j != 5):
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
    
    def interact(self, GETR):
        x = GETR.getX()
        y = GETR.getY()
        ID = self.getCellID(x, y)
        data = jsonHandler.getDataFromFile("mapData.json")
        nameOfMaterial = data["ids"][ID]["name"]
        amountToAdd = random.randrange(0, 4)
        GETR.setInventorySlot(nameOfMaterial, amountToAdd)
        print(str(amountToAdd) + " " + nameOfMaterial + "s obtained!")
        #empty out the cell:
        self.setCellID(x, y, 0)
        return
