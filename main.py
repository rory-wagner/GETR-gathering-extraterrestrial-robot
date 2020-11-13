import robot
import tutorial
import jsonHandler
import string

def getValidActionFromUser(GETR, placeToCheckValidity):
    while True:
        userInput = input("->").lower()
        canDo = placeToCheckValidity.isValidMove(GETR, userInput)
        if canDo:
            return userInput
        else:
            print("Please type in a valid option. Type 'h' for help")

def moveUp(GETR, currentMap):
    y = GETR.getY()
    y -= 1
    GETR.setY(y)

def moveLeft(GETR, currentMap):
    x = GETR.getX()
    x -= 1
    GETR.setX(x)

def moveDown(GETR, currentMap):
    y = GETR.getY()
    y += 1
    GETR.setY(y)

def moveRight(GETR, currentMap):
    x = GETR.getX()
    x += 1
    GETR.setX(x)

def doAction(GETR, currentMap, action):
    allActions = {
        "w": moveUp,
        "a": moveLeft,
        "s": moveDown,
        "d": moveRight,
    }
    for a in allActions:
        if a == action:
            allActions[a](GETR, currentMap)


def mainLoop(GETR, personalShip, currentSector):
    while True:
        onPlanet = GETR.getOnPlanet()
        selectedAction = ""
        if onPlanet:
            selectedAction = getValidActionFromUser(GETR, currentSector)
            doAction(GETR, currentSector, selectedAction)
        else:
            selectedAction = getValidActionFromUser(GETR, personalShip)
            doAction(GETR, personalShip, selectedAction)

    return

def enterTutorial():
    return

def main():
    GETR = robot.Robot()
    # personalShip = ship.Ship()
    # currentSector = sector.Sector()
    enterTutorial(GETR, personalShip, currentSector)
    mainLoop(GETR, personalShip, currentSector)

