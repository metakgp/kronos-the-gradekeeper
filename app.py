from flask import Flask, request,render_template, url_for, redirect, send_file, send_from_directory
import string
import json
from SearchGrades import SearchGrades
from MakeGraphs import MakeGraphs

app = Flask(__name__)
numberRecords=0
jsonFile = open("courses.json", "r")
data = json.load(jsonFile)
jsonFile.close()
courses=[]
for key in data:
    string =""
    string = data[key]["id"] + " : " + data[key]["name"]
    courses.append(string)
#print(courses)
Grades = {}
@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == "POST":
        code = request.form.get('getCode')
        code = code.upper()
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
            #MakeGraphs(Grades,code)
            return render_template('kronos.html',courseCode = code, Grades = Grades, result = "show-grades",courses = courses)

    else:
        code ="skf"
        Grades = {}
        return render_template('kronos.html',courseCode = '', Grades = Grades, result = "",courses = courses)


#@app.route('/figure/<filename>')
#def figure(filename):
#   return send_from_directory('figure', filename)


if __name__=="__main__" :
    app.run()
else:
    #print ("/n /n /n hmmmm  ") 
    print(__name__)