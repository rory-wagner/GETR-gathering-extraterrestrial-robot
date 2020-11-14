import gridMap
import jsonHandler
import random

class Sector(gridMap.GridMap):
    def __init__(self, width, height, planet):
        gridMap.GridMap.__init__(self, 11, 11)
        self.planet = planet
        self.map[6][6] = 1
        self.generateMap(self.planet)


    def generateMap(self, planet):
        data = jsonHandler.getDataFromFile("planetData.json")
        concentrations = data["locationList"][planet][concentration]
        for i in range(self.width):
            for j in range(self.height):
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

