from stringcolor import * 
import robot
import jsonHandler
 
class GridMap:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.map = self.createMapArray()
        self.visitedMap = self.createVisitedMapArray()
        self.planet = "Default"

    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height

    def createMapArray(self):
        prepList = []
        for i in range(self.width):
            holdList = [0] * self.height
            prepList.append(holdList)
        return prepList
    
    def createVisitedMapArray(self):
        prepList = []
        for i in range(self.width):
            holdList = [False] * self.height
            prepList.append(holdList)
        return prepList

    def populateMap(self):
        # This will place all of the materials and encounters on the map
        return
    
    def display(self, robot):
        cross = u'\u253C'
        HLine = u'\u2500'
        Vline = u'\u2502'
        DownT = u'\u252C'
        RightT= u'\u2524'
        LeftT = u'\u251C'
        UpT   = u'\u2534'
        TLCor = u'\u250C'
        TRCor = u'\u2510'
        BLCor = u'\u2514'
        BRCor = u'\u2518'
        palette =  [
            cross, HLine, Vline, DownT, LeftT,
            RightT, UpT, TLCor, TRCor, BLCor, BRCor
        ]
        self.printLines(robot)
        
    def colorizeAndPrint(self, lines):
        
        for line in lines:
            if ((line[0] == u'\u250C') or (line[0] == u'\u2514') or (line[0] == u'\u251C')):
                print(cs(line, color))
            else:
                holdstring = ""
                for char in line:
                    if (line[char] == u'\u2502'):
                        print(cs(line[char], color), sep="")
                    elif (line[char] == " "):
                        print(line[char])
                        if holdstring != "":
                            data = jsonHandler.getDataFromFile("mapData.json")
                            checkList = data["ids"]
                            color = ""
                            for key in checkList:
                                if checkList[key]["mapRep"] == holdstring or checkList[key]["mapRep"] == holdstring[:-1]:
                                    color = checkList[key]["color"]
                            print(cs(holdstring, color))
                            holdstring = ""
                    else:
                        holdstring += line[char]

    def printLines(self, robot):
        self.createTopLine()
        for i in range(self.height):

            self.createMidLines(robot, i)

            if i == self.height - 1:
                self.createBotLine()
            else:
                self.createSepLine()
    
    def createTopLine(self):
        TLCor = u'\u250C'
        TRCor = u'\u2510'
        HLine = u'\u2500'
        DownT = u'\u252C'
        linebuffer = []
        linebuffer.append(TLCor)
        for i in range(self.width):
            linebuffer.append(HLine + HLine + HLine + HLine + HLine + HLine + HLine)

            if i == self.width - 1:
                linebuffer.append(TRCor)
            else:
                linebuffer.append(DownT)

        finalLine = ""
        for item in linebuffer:
            finalLine += item
        data = jsonHandler.getDataFromFile("planetData.json")
        color = data["locationList"][self.planet]["color"]
        print(cs(finalLine, color))

    def createMidLines(self, robot, y):
        Vline = u'\u2502'
        data = jsonHandler.getDataFromFile("planetData.json")
        planetColor = data["locationList"][self.planet]["color"]

        # Print Top Blank line
        print(cs(Vline, planetColor), end="")
        for i in range(self.width):
            print("       ", end="")
            if i == self.width - 1:
                print(cs(Vline, planetColor))
            else:
                print(cs(Vline, planetColor), end="")

        # Print Content line
        print(cs(Vline, planetColor), end="")

        for i in range(self.width):
            id = self.getLocationID(i, y)
            rep = self.getMapRep(id, i, y)

            if self.robotIn(robot, i, y):
                totalspaces = 8 - len(rep) - 1
                rep += "*"
            else:
                totalspaces = 8 - len(rep)

            if totalspaces % 2 == 0:
                prespaces = totalspaces / 2
                postspaces = totalspaces / 2 - 1
            else:
                prespaces = totalspaces / 2
                postspaces = prespaces

            for j in range(int(prespaces)):
                print(" ", end="")

            data = jsonHandler.getDataFromFile("mapData.json")
            checkList = data["ids"]
            color = ""
            if self.robotIn(robot, i, y):
                for key in checkList:
                    if key["mapRep"] == rep[:-1]:
                        color = key["color"]
            else:
                for key in checkList:
                    if key["mapRep"] == rep:
                        color = key["color"]

            print(cs(rep, color), end="")

            for j in range(int(postspaces)):
                print(" ", end="")

            if i == self.width - 1:
                print(cs(Vline, planetColor))
            else:
                print(cs(Vline, planetColor), end="")

        # Print Bottom Blank line

        print(cs(Vline, planetColor), end="")
        for i in range(self.width):
            print("       ", end="")
            if i == self.width - 1:
                print(cs(Vline, planetColor))
            else:
                print(cs(Vline, planetColor), end="")

    def robotIn(self, robot, x, y):
        if(robot.getX() == x) and (robot.getY() == y):
            return True
        else:
            return False

    def createSepLine(self):
        cross = u'\u253C'
        RightT= u'\u2524'
        LeftT = u'\u251C'
        HLine = u'\u2500'
        data = jsonHandler.getDataFromFile("planetData.json")
        planetColor = data["locationList"][self.planet]["color"]
        sepLineBuffer = []
        sepLineBuffer.append(LeftT)
        for i in range(self.width):
            sepLineBuffer.append(HLine + HLine + HLine + HLine + HLine + HLine + HLine)
            if i == self.width - 1:
                sepLineBuffer.append(RightT)
            else:
                sepLineBuffer.append(cross)
        finalSep = ""
        for item in sepLineBuffer:
            finalSep += item
        print(cs(finalSep, planetColor))

    def createBotLine(self):
        BLCor = u'\u2514'
        BRCor = u'\u2518'
        HLine = u'\u2500'
        UpT   = u'\u2534'
        data = jsonHandler.getDataFromFile("planetData.json")
        planetColor = data["locationList"][self.planet]["color"]
        linebuffer = []
        linebuffer.append(BLCor)
        for i in range(self.width):
            linebuffer.append(HLine + HLine + HLine + HLine + HLine + HLine + HLine)
            if i == self.width - 1:
                linebuffer.append(BRCor)
            else:
                linebuffer.append(UpT)
        finalLine = ""
        for item in linebuffer:
            finalLine += item
        print(cs(finalLine, planetColor))

    def getMapRep(self, id, x, y):
        # goes to map data looks at id
        # if not visited return blank string
        # else return the string of the representation
        if self.checkVisited(x, y):
            data = jsonHandler.getDataFromFile("mapData.json")
            return data["ids"][id]["mapRep"]
        else:
            return ""

    def checkVisited(self, x, y):
        # checks if location is visited, returns bool
        if self.visitedMap[x][y] == True:
            return True
        else:
            return False

    def getColor(self, robot):
        # gets the location of the robot and looks up
        # the color that is set for the planet
        return color

    def isValidMove(self, robot, action, extraOptions):
        # receives a robot object and action as lowercase string
        # returns bool
        contentsId = self.getLocationID(robot.getX(), robot.getY())
        data = jsonHandler.getDataFromFile("mapData.json")
        actions = data["ids"][contentsId]["validActions"]
        if robot.getY() < self.height - 1:
            actions.append("s")
        if robot.getY() > 0:
            actions.append("w")
        if robot.getX() < self.width - 1:
            actions.append("d")
        if robot.getX() > 0:
            actions.append("a")
        for opt in extraOptions:
            actions.append(opt)
        if action in actions:
            return True
        else:
            return False

    def getValidOptions(self, robot):
        # receives a robot object
        # return a list of strings representing valid actions
        contentsId = self.getLocationID(robot.getX(), robot.getY())
        data = jsonHandler.getDataFromFile("mapData.json")
        return data["ids"][contentsId]["validActions"]

    def getLocationID(self, x, y):
        # receives a location
        # returns the int of the id that exists at location
        return self.map[x][y]

