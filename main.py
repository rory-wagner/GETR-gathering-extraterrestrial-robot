import robot
import tutorial
import jsonHandler
import string
import gridMap
import inputConsole

def getValidActionFromUser(GETR, placeToCheckValidity):
    while True:
        userInput = inputConsole.getInput().lower()
        extraValidOptions = ["m"]
        canDo = placeToCheckValidity.isValidMove(GETR, userInput, extraValidOptions)
        if canDo:
            return userInput
        else:
            print("Please type in a valid option. Type 'h' for help")

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
    else:
        return userOption

def displayMap(GETR, currentMap):
    currentMap.display(GETR)
    return

def doAction(GETR, currentMap, action):
    allActions = {
        "w": moveUp,
        "a": moveLeft,
        "s": moveDown,
        "d": moveRight,
        "e": interact,
        "m": displayMap,
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
    currentSector = sector.Sector()

    # print a beginning to the tutorial
    enterTutorial(GETR, personalShip, currentSector)

    #print a beginning to the real game
    mainLoop(GETR, personalShip, currentSector)
    return

#testing for now:

def test():
    GETR = robot.Robot()
    ourMap = gridMap.GridMap(10, 10)
    mainLoop(GETR, ourMap, ourMap)
    return

test()
