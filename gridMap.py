from stringcolor import * 
import robot
import jsonHandler
 
class GridMap:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.map = self.createMapArray()
        self.visitedMap = self.createVisitedMapArray()
        
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
        lines = self.prepLines(robot)
        something = ""
        color = self.getColor(something)
        for line in lines:
            print(cs(line, color))

    def prepLines(self, robot):
        buffer = []
        buffer.append(self.createTopLine())
        for i in range(self.height):

            buffer.append(self.createMidLines(robot, i))

            if i == self.height - 1:
                buffer.append(self.createBotLine())
            else:
                buffer.append(self.createSepLine())

        return buffer
    
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

        return finalLine

    def createMidLines(self, robot, y):
        Vline = u'\u2502'
        mainLineBuffer = []
        blankLineBuffer = []
        mainLineBuffer.append(Vline)
        blankLineBuffer.append(Vline)
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
                mainLineBuffer.append(" ")
            mainLineBuffer.append(rep)

            for j in range(int(postspaces)):
                mainLineBuffer.append(" ")

            mainLineBuffer.append(Vline)
            blankLineBuffer.append("       ")
            blankLineBuffer.append(Vline)
        finalMainLine = ""
        finalBlankLine = ""
        for item in mainLineBuffer:
            finalMainLine += item
        for other in blankLineBuffer:
            finalBlankLine += other
        #This combines all the 3 lines into one string to send to the buffer
        finalLine = finalBlankLine + "\n" + finalMainLine + "\n" + finalBlankLine
        return finalLine

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
        return finalSep

    def createBotLine(self):
        BLCor = u'\u2514'
        BRCor = u'\u2518'
        HLine = u'\u2500'
        UpT   = u'\u2534'
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
        return finalLine

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
        return "White"

    def isValidMove(self, robot, action):
        # receives a robot object and action as lowercase string
        # returns bool
        contentsId = self.getLocationID(robot.getX, robot.getY)
        data = jsonHandler.getDataFromFile("mapData.json")
        actions = data["ids"][contentsId]["validActions"]
        if action in actions:
            return True
        else:
            return False

    def getValidOptions(self, robot):
        # receives a robot object
        # return a list of strings representing valid actions
        contentsId = self.getLocationID(robot.getX, robot.getY)
        data = jsonHandler.getDataFromFile("mapData.json")
        return data["ids"][contentsId]["validActions"]

    def getLocationID(self, x, y):
        # receives a location
        # returns the int of the id that exists at location
        return self.map[x][y]

