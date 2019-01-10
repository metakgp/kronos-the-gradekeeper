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
        code = "".join(code.split())
        code = code[:7]
        Courselink = ""
        with open("data_file.json","r") as read_file:
            data = json.load(read_file)
        for key in data.keys():
            if(key == code ):
                Courselink = "https://wiki.metakgp.org" + data[key]
        Grades = SearchGrades(code)
        numberRecords = len (Grades)
        
        if( Grades == 'NA'):

            if len (code) == 7 and code[:2].isalpha() and code[-5:].isdigit() :
                return render_template('kronos.html',courseCode = code, Grades = Grades, result = "no-data", courses = courses)
            else:
                return render_template('kronos.html',courseCode = code, Grades = Grades, result = "invalid-code", courses = courses)
        
        else:
            return render_template('kronos.html',courseCode = code, Grades = Grades, result = "show-grades",courses = courses, Cwikilink = Courselink)

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
