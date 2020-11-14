import jsonHandler
import random
import sector
import robot
import inputConsole
from stringcolor import *

def getScenarioNum(allScenarios):
    return random.randrange(0, len(allScenarios))

def printMessageToUser(currScenario):
    print(cs(currScenario["messageToUser"], "DodgerBlue2"))

def getValidOption(GETR, currScenario):
    while True:
        userInput = inputConsole.getInput()
        if userInput in currScenario["optionsSelect"]:
            return userInput
        else:
            print(cs("Please type in a valid option.", "Red"))
            for opt in currScenario["optionsSelect"]:
                print(cs(opt, "DodgerBlue"))

def useShocker(GETR, currSector):
    return
def usePay(GETR, currSector):
    return
def useRun(GETR, currSector):
    return

def checkSuccessOrFailure(GETR, currSector, currScenario, userOption):
    successRate = 0
    theIndex = None
    for i in range(len(currScenario["optionsSelect"])):
        if currScenario["optionsSelect"][i] == userOption:
            successRate = currScenario["successRates"][i]
            theIndex = i
    roll = random.randrange(0, 100)
    if roll <= successRate:
        #success
        if userOption != "r":
            GETR.setByteCoins(GETR.getByteCoins() + currScenario["moneyRewardOrLoss"])
            print(cs(currScenario["successMessages"][theIndex], "SpringGreen6"))
            print(cs("Total Bytecoins: " + str(GETR.getByteCoins()), "Gold2"))
        else:
            #if they run, don't gain money
            print(currScenario["successMessages"][theIndex])
            # GETR.setByteCoins(GETR.getByteCoins() + currScenario["moneyRewardOrLoss"])
            # print(GETR.getByteCoins())
    else:
        #failure
        try:
            GETR.setByteCoins(GETR.getByteCoins() - currScenario["moneyRewardOrLoss"])
        except:
            GETR.setByteCoins(0)
        print(cs(currScenario["failureMessages"][theIndex], "IndianRed"))
        print(cs("Total Bytecoins: " + str(GETR.getByteCoins()), "Gold2"))

#the organization of data in scenarios.json is as follows:
# [
#     {
#         messageToUser: message *str*,
#         optionsSelect: lst *list of str*
#         successRates: lst *list of int*
#         moneyRewardOrLoss: *int*
#         successMessages: lst *list of str*
#         failureMessages: lst *list of str*
#     }
# ]
def performRandomScenario(GETR, currSector):
    allScenarios = jsonHandler.getDataFromFile("scenarios.json")
    randScenNum = getScenarioNum(allScenarios)
    currScenario = allScenarios[randScenNum]

    printMessageToUser(currScenario)
    userOption = getValidOption(GETR, currScenario)

    checkSuccessOrFailure(GETR, currSector, currScenario, userOption)
    
    return


