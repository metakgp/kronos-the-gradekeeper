from flask import Flask, request,render_template, url_for, redirect, send_file, send_from_directory
import string

from SearchGrades import SearchGrades
from MakeGraphs import MakeGraphs

app = Flask(__name__)
numberRecords=0

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == "POST":
        code = request.form.get('getCode')
        code = code.upper()
        code = "".join(code.split())

        Grades = SearchGrades(code)
        numberRecords = len (Grades)
        
        if( Grades == 'NA'):

            if len (code) == 7 and code[:2].isalpha() and code[-5:].isdigit() :
                return render_template('kronos.html',courseCode = code, numberRecords = numberRecords,result = "no-data")
            else:
                return render_template('kronos.html',courseCode = code, numberRecords = numberRecords,result = "invalid-code")
        
        else:
            MakeGraphs(Grades,code)
            return render_template('kronos.html',courseCode = code, numberRecords = numberRecords,result = "show-grades")

    else:
        code ="skf"
        return render_template('kronos.html',courseCode = '', numberRecords = '',result = "")


@app.route('/figure/<filename>')
def figure(filename):
    return send_from_directory('figure', filename)


if __name__=="__main__" :
    app.run()
else:
    #print ("/n /n /n hmmmm  ") 
    print(__name__)