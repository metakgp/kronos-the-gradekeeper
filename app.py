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
        c2=code
        #To extract Name of Course
        c3=c2.split(":")
        c3=c3[1]
        c3=c3[1:]
        c4=c3
        #Forming a string which can be used as a link
        string=""
        for i in range(0,len(c3)):
            if(i==0):
                string=string+"_"+c3[i]
            elif(c3[i]==" "):
                string=string+"_"+c3[i+1]
            elif(c3[i-1]!=" "):
                string=string+c3[i].lower()
        c3=string
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
            return render_template('kronos.html',courseCode = code, Grades = Grades, result = "show-grades",courses = courses,c1=c3,c5=c4)

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
