import json

def getDataFromFile(fileName):
    with open(fileName) as jsonFile:
        jsonData = json.load(jsonFile)
        return jsonData
