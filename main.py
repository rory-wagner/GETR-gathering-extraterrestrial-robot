import robot
import tutorial
import jsonHandler
import string
import gridMap

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

def interact(GETR, currentMap):
    #gives back a call-back function
    userOption = currentMap.interact(GETR)

def doAction(GETR, currentMap, action):
    print("doing Action")
    allActions = {
        "w": moveUp,
        "a": moveLeft,
        "s": moveDown,
        "d": moveRight,
        "e": interact,
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
