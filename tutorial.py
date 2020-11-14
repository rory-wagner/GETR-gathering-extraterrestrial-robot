from stringcolor import *
import time
import ship
import sector
import robot

def intro():
    print(" \t \t ", end="")
    message = "Greetings program ..."
    for i in range(len(message)):
        print(cs(message[i], "Green3"), end="")
    print()
    time.sleep(1)


def teachCommands():
    return

def teachShip():
    return

def teachMaterials():
    return

def teachPlanets():
    return

def showQuest():
    return

def showShop():
    return



def begin():
    intro()
    teachCommands()
    teachShip()
    teachMaterials()
    teachPlanets()
    showQuest()
    showShop()


begin()