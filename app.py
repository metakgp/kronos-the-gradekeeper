from flask import Flask, request,render_template, url_for, redirect, send_file, send_from_directory
import string
import json
from SearchGrades import SearchGrades


app = Flask(__name__)
numberRecords=0
jsonFile = open("Grades/yearWiseGrades.json", "r")
data = json.load(jsonFile)
jsonFile.close()
courses=[]
with open("courses.json","r") as f:
    courses_having_data = json.load(f)
    for key in data:

        string =""
        try:
            string = key + " : " + courses_having_data[key]["name"]
        except:
            string = key
        courses.append(string)

Grades = {}

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == "POST":
        code = request.form.get('getCode')
        code = code.upper()
        #Extratcing name of course for wiki links
        Course_info=code
        #To extract Name of Course
        Course_info = Course_info.split(":")[1][1:]
        CourseName = Course_info
        #Forming a string which can be used as a link
        course_info_wiki_link = ""
        for i in range(0,len(Course_info)):
            if(i == 0):
                course_info_wiki_link = course_info_wiki_link + "_"+ Course_info[i]
            elif(Course_info[i] == " "):
                course_info_wiki_link = course_info_wiki_link + "_" + Course_info[i+1]
            elif(Course_info[i-1] != " "):
                course_info_wiki_link=course_info_wiki_link+Course_info[i].lower()
        Course_info = course_info_wiki_link
        code = "".join(code.split())
        code = code[:7]
        Grades = SearchGrades(code)
        numberRecords = len (Grades)
        
        if( Grades == 'NA'):

            if len (code) == 7 and code[:2].isalpha() and code[-5:].isdigit() :
                return render_template('kronos.html',courseCode = code, Grades = Grades, result = "no-data", courses = courses)
            else:
                return render_template('kronos.html',courseCode = code, Grades = Grades, result = "invalid-code", courses = courses)
        
        else:
            return render_template('kronos.html',courseCode = code, Grades = Grades, result = "show-grades",courses = courses,Cwikilink=Course_info,CoursN=CourseName)

    else:
        Grades = {}
        return render_template('kronos.html',courseCode = '', Grades = Grades, result = "on-start",courses = courses)


#@app.route('/figure/<filename>')
#def figure(filename):
#   return send_from_directory('figure', filename)


if __name__=="__main__" :
    app.run()
else:
    #print ("/n /n /n hmmmm  ") 
    print(__name__)
