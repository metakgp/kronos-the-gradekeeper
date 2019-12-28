#This file searches for the requested course from the json file containing combined grades and returns dict for graphs to be made.
import json

def SearchGrades(courseCode):
    jsonFile = open("data/Grades/yearWiseGrades.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()

    try:
        courseMatched = data[courseCode]
    except:
        courseMatched = 'NA'

    return(courseMatched)
