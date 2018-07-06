from flask import Flask, request,render_template, url_for, redirect, send_file, send_from_directory
import string

from SearchGrades import SearchGrades
from MakeGraphs import MakeGraphs



app = Flask(__name__)



@app.route('/', methods = ['GET','POST'])
def home():s
    if request.method == "POST":
        code = request.form.get('getCode')
        code = code.upper()
        code = "".join(code.split())
        print (code)

        Grades = SearchGrades(code)
        numberRecords = len (Grades)
        print '\n\n\n\n\n'
        print (Grades)
        print (numberRecords)
        print '\n\n\n\n\n'
        if( Grades == 'NA'):

            if len (code) == 7 and code[:2].isalpha() and code[-5:].isdigit() :
                return render_template('no_data.html',output = '')
            else:
                return render_template('invalid_code.html',output = '')
        
        else:
            MakeGraphs(Grades,code)
            return render_template('result.html',courseCode = code, numberRecords = numberRecords)

    else:
        return render_template('grim_reaper.html', output = '')

@app.route('/invalid_code')    
def invalid_code():    
    return render_template('invalid_code.html',output = '')

@app.route('/figure/<filename>')
def figure(filename):
    
    #img = StringIO()
    #im = Image.open("./Grades/combinedGrades.png")
    #img = im
    #img.seek(0)
    return send_from_directory('figure', filename)


if __name__=="__main__" :
    app.run()
else :
    app.run()