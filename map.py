from stringcolor import * 
 
class map:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.map = self.createMapArray()
        self.visited = self.createMapArray()
        self.populateMap()
        self.display()

    def createMapArray(self):
        prepList = []
        for i in range(self.width):
            holdList = [0] * self.height
            prepList.append(holdList)
        return prepList
    
    def populateMap(self):
        # This will place all of the materials and encounters on the map
        return
    
    def display(self):
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
        lines = self.prepLines()
        something = ""
        color = self.getColor(something)
        for line in lines:
            print(cs(line, color))

    def prepLines(self):
        buffer = []
        buffer.append(self.createTopLine())
        for i in range(self.height):
            buffer.append(self.createMidLines(i))
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

    def createMidLines(self, y):
        Vline = u'\u2502'
        mainLineBuffer = []
        blankLineBuffer = []
        mainLineBuffer.append(Vline)
        blankLineBuffer.append(Vline)
        for i in range(self.width):
            id = self.getLocationID(i, y)
            rep = self.getMapRep(id)
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

    def getMapRep(self, id):
        # goes to map data looks at id
        # if visited return blank string
        # else return the string of the representation
        return ""

    def getColor(self, robot):
        # gets the location of the robot and looks up
        # the color that is set for the planet
        return "White"

    def isValidMove(self, robot, action):
        # receives a robot object and action as lowercase string
        # returns bool
        return

    def getValidOptions(self, robot):
        # receives a robot object
        # return a list of strings representing valid actions
        return

    def getLocationID(self, x, y):
        # receives a location
        # returns the int of the id that exists at location
        return
    
m = map(2,2)