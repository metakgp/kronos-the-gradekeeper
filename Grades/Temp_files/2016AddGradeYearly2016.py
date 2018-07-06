import json

def addNewCourse(course,grades,year):
    jsonFile = open("yearWiseGrades.json", "r")
    data_main = json.load(jsonFile)
    jsonFile.close()

    addCourse={}  
    addCourse[year] = grades
    data_main[course]= addCourse
    print(data_main)
    
    jsonFile = open("yearWiseGrades.json", "w+")
    jsonFile.write(json.dumps(data_main))
    jsonFile.close()

    #with open('yearWiseGrades.json',) as json_file_main:
        #data_main = json.load (json_file_main)
        #addCourse={}
        #addCourse[keys] = {}
        #addCourse[keys][year] = value['grades']
        #print (addData)
        #json.dump(addData, outfile)

def addGrade(keys,value,year):
    with open('yearWiseGrades.json') as json_file_main:
        data_main = json.load (json_file_main)
        
        courseMatched = False

        for keys_main, value_main in data_main.iteritems():
            if keys == keys_main:
                value_main['year'] = value
                courseMatched = True
                break

        if courseMatched == False:
            addNewCourse(keys,value,year)
            with open('yearWiseGrades.json') as jsonf:
                data_f = json.load (jsonf)
                print(data_f)



def read_file(filename):
    with open('%s.json' % filename) as json_file:  
        data = json.load(json_file)

        for keys, value in data.iteritems():
            addGrade(keys,value,filename)
    
read_file('2016Spring')
