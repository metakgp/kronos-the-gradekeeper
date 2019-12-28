#This python file merges the data from individual semester record containing json files into
#into yearWiseGrades.json. This will result in faster searching.
import json
import os


def addNewCourse(course,grades,year): #This function is meant for new courses for which there wasnt any info
    jsonFile = open("yearWiseGrades.json", "r")
    data_main = json.load(jsonFile)
    jsonFile.close()

    addCourse={}  
    addCourse[year] = grades['grades']
    data_main[course]= addCourse
    
    jsonFile = open("yearWiseGrades.json", "w+")
    jsonFile.write(json.dumps(data_main))
    jsonFile.close()


def addGrade(keys,value,year):
    
    
    json_file_main = open("yearWiseGrades.json", "r")
    data_main = json.load (json_file_main)
    json_file_main.close()
    
    courseMatched = False

    for keys_main, value_main in data_main.iteritems():
        if keys == keys_main:
            data_main[keys_main][year] = value['grades']
            courseMatched = True
            break

    json_file_main = open("yearWiseGrades.json", "w+")
    json_file_main.write(json.dumps(data_main))
    json_file_main.close()

    if courseMatched == False:
        addNewCourse(keys,value,year)
        with open('yearWiseGrades.json') as jsonf:
            data_f = json.load (jsonf)


def read_file(filename):
    os.chdir(os.getcwd() + '/Grades')
    with open(os.getcwd() +'/past_records/' + filename + '.json' ) as json_file:  
        data = json.load(json_file)
        for keys, value in data.iteritems():
            addGrade(keys,value,filename)
    
#read_file('2000Spring')
