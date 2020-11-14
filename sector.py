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
                for key in concentrations:
                    if random.randrange(0, 100) <= concentrations[key]:
                        self.map[i][j] = key
                        break