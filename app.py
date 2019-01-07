from flask import Flask, request,render_template, url_for, redirect, send_file, send_from_directory
import string
import json
from SearchGrades import SearchGrades
from bs4 import BeautifulSoup
import requests 
import re

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
        #To Extract Course Wiki links
        Courselink = ""
        courseFile = requests.get("https://wiki.metakgp.org/index.php?title=Category:Courses")
        soup=BeautifulSoup(courseFile.text,'html.parser')
        coursecodes = []
        pattern="[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]"
        for a in soup.find_all('a',href = True):
            if(re.search(pattern,a['href'][3:10])):
                coursecodes.append(a['href'])
        for i in range(2,201):
            for a in soup.find_all('a',href = True,text = 'next page'):
                nextpagelink = a['href']
                courseFile=requests.get("https://wiki.metakgp.org"+nextpagelink)
                soup=BeautifulSoup(courseFile.text,'html.parser')
                pattern="[A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]"
            for a in soup.find_all('a',href = True):
                if(re.search(pattern,a['href'][3:10])):
                    coursecodes.append(a['href'])
        for i in range(len(coursecodes)):
            if(code == coursecodes[i][3:10]):
                Courselink = "https://wiki.metakgp.org"+ coursecodes[i]
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
