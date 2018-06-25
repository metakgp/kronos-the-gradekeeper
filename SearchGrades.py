import json

def SearchGrades(courseCode):
    jsonFile = open("Grades/yearWiseGrades.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    try:
        courseMatched = data[courseCode]
    except:
        courseMatched = 'NA'
    
    print(courseMatched)

#SearchGrades('CH62028')
