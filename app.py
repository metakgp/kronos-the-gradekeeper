from flask import Flask, request,render_template, url_for
from SearchGrades.py import SearchGrades
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    print 'yo'
    if request.method == "POST":
        code = request.form.get('coursecode')
        print (code)
        code = r'<script>alert("Result: {}")</script>'.format(code)
         return render_template('grim_reaper.html', output = code)
     else:
        return render_template('grim_reaper.html', output = '')

if __name__=="__main__" :
    app.run()
