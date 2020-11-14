import robot
import tutorial
import jsonHandler
import string
# import gridMap
import ship
import sector
import inputConsole
from stringcolor import *

def getValidActionFromUser(GETR, placeToCheckValidity):
    while True:
        userInput = inputConsole.getInput().lower()
        extraValidOptions = ["m", "h"]
        canDo = placeToCheckValidity.isValidMove(GETR, userInput, extraValidOptions)
        if canDo:
            return userInput
        else:
            GETR.incConfusedCounter()
            TLCor = u'\u250C'
            TRCor = u'\u2510'
            BLCor = u'\u2514'
            BRCor = u'\u2518'
            HLine = u'\u2500'
            Vline = u'\u2502'
            messages = [
                "Huh? Aww the simple little GETR is trying to communicate. Type 'h' if your not sure what to input.",
                "Almost there. Just one byte more... Nope. Missed it by half a pixel. FacePalm.exe Initiated ...",
                "I told you already, type 'h' if you are confused",
                "I am disappointed GETR. Either your programming is corrupted or your neural network is underdeveloped."
            ]
            line = Vline + messages[GETR.getConfusedCounter() % len(messages)] + Vline
            linelen = len(line)

            topLine = TLCor 
            for i in range(linelen - 2):
                topLine += HLine
            topLine += TRCor

            print(cs(topLine, "SteelBlue"))

            print(cs(line, "SteelBlue"))
        
            botLine = BLCor 
            for i in range(linelen - 2):
                botLine += HLine
            botLine += BRCor
            print(cs(botLine, "SteelBlue"))
        

def moveUp(GETR, currentMap):
    y = GETR.getY()
    y -= 1
    GETR.setY(currentMap, y)


def moveLeft(GETR, currentMap):
    x = GETR.getX()
    x -= 1
    GETR.setX(currentMap, x)


def moveDown(GETR, currentMap):
    y = GETR.getY()
    y += 1
    GETR.setY(currentMap, y)


def moveRight(GETR, currentMap):
    x = GETR.getX()
    x += 1
    GETR.setX(currentMap, x)

def interact(GETR, currentMap):
    #gives back a call-back function
    userOption = currentMap.interact(GETR)
    if userOption == "Exit":
        GETR.setOnPlanet(True)
        GETR.setX(currentMap, 5)
        GETR.setY(currentMap, 5)
        currentMap.setVisited(5, 5)
    else:
        return userOption

def displayMap(GETR, currentMap):
    currentMap.setVisited(GETR.getX(), GETR.getY())
    currentMap.display(GETR)
    return

def helpMenu(GETR, currentMap):
    color = "IndianRed3"
    HLine = u'\u2500'
    Vline = u'\u2502'
    RightT= u'\u2524'
    LeftT = u'\u251C'
    TLCor = u'\u250C'
    TRCor = u'\u2510'
    BLCor = u'\u2514'
    BRCor = u'\u2518'
    skip = " "

    topLine = TLCor 
    for i in range(45):
        topLine += HLine
    topLine += TRCor

    helpTitle = Vline
    for i in range(21):
        helpTitle += skip 
    helpTitle += "HELP" 
    for i in range(20):
        helpTitle += skip 
    helpTitle += Vline

    separator = LeftT
    for i in range(45): 
        separator += HLine
    separator += RightT

    wline = Vline + "'w' key ----------------- Moves your GETR up."+ Vline
    aline = Vline + "'a' key --------------- Moves your GETR left."+ Vline
    sline = Vline + "'s' key --------------- Moves your GETR down."+ Vline
    dline = Vline + "'d' key -------------- Moves your GETR right."+ Vline
    eline = Vline + "'e' key - Interact with room where your GETR."+ Vline
    mline = Vline + "'m' key --- Mine resource where your GETR is."+ Vline
    hline = Vline + "'h' key ------------ Displays this help menu."+ Vline

    botLine = BLCor 
    for i in range(45):
        botLine += HLine
    botLine += BRCor


    buffer= [
        topLine, helpTitle, 
        separator, wline, 
        aline, sline, 
        dline, eline, 
        mline, hline,
        botLine
        ]

    for line in buffer:
        print(cs(line, color))


def doAction(GETR, currentMap, action):
    allActions = {
        "w": moveUp,
        "a": moveLeft,
        "s": moveDown,
        "d": moveRight,
        "e": interact,
        "m": displayMap,
        "h": helpMenu,
    }
    for a in allActions:
        if a == action:
            return allActions[a](GETR, currentMap)


def mainLoop(GETR, personalShip, currentSector):
    while True:
        onPlanet = GETR.getOnPlanet()
        selectedAction = ""
        if onPlanet:
            selectedAction = getValidActionFromUser(GETR, currentSector)
            doAction(GETR, currentSector, selectedAction)
        else:
            selectedAction = getValidActionFromUser(GETR, personalShip)
            possibleSector = doAction(GETR, personalShip, selectedAction)
            if possibleSector != None:
                currentSector.generateMap(possibleSector)

    return

def enterTutorial():
    return

def main():
    GETR = robot.Robot()
    personalShip = ship.Ship()
    #width, height, and planet
    currentSector = sector.Sector(11, 11, "Earth")

    # print a beginning to the tutorial
    # enterTutorial(GETR, personalShip, currentSector)

    #print a beginning to the real game
    mainLoop(GETR, personalShip, currentSector)
    return

main()

#testing for now:

# def test():
#     GETR = robot.Robot()
#     ourMap = gridMap.GridMap(10, 10)
#     mainLoop(GETR, ourMap, ourMap)
#     return

# test()
