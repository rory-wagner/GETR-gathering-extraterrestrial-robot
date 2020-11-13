import gridMap

class Sector(gridMap.GridMap):
    def __init__(self, width, height):
        gridMap.GridMap.__init__(self, width, height)

    def generateMap(self):
        return