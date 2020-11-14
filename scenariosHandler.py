import jsonHandler
import random
import sector
import robot
import inputConsole

def getScenarioNum(allScenarios):
    return random.randrange(0, len(allScenarios))

def printMessageToUser(currScenario):
    print(currScenario["messageToUser"])

def getValidOption(GETR, currScenario):
    while True:
        userInput = inputConsole.getInput().lower()
        if userInput in currScenario["optionsSelect"]:
            return userInput
        else:
            print("Please type in a valid option.")
            for opt in currScenario["optionsSelect"]:
                print(opt)

def useShocker(GETR, currSector):
    return
def usePay(GETR, currSector):
    return
def useRun(GETR, currSector):
    return

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

    userSuccess = checkSuccessOrFailure(GETR, currSector, currScenario, userOption)

    allOptions = {
        "z": useShocker,
        "p": usePay,
        "r": useRun
    }
    for opt in allOptions:
        if opt == userOption:
            allOptions[opt](GETR, currSector)
    
    return


