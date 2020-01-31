from flask import Flask, render_template, request, redirect, jsonify
import shutil
import json

app = Flask(__name__)
UPLOAD_FOLDER = '/file'
app.secret_key = "XENIA"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

color = '#5bc0de'
imgpath = ''

@app.route('/result',methods = ['POST', 'GET'])
def getuser():
   if request.method == 'POST':
       global color
       global imgpath
       result = request.form

       msg = list()
       editlist = [result['Title'], str(color), str(color), result['Title'],str(color),
                   result['Name'], result['TEXT'], result['location'], result['email'],
                   str('https://github.com/')+result['GithubID'], result['facebook'], result['GithubID']
                   ]
       for x in range(1,14):
           filename = 'index_gen/' + str(x)
           f = open(filename, 'r')
           msg.append(f.read().replace('\n',''))
           f.close()

       lastm = ''
       for x in range(12):
           m = msg[x] + editlist[x]
           lastm += m
       lastm += msg[-1]

       f = open("output/index.html", 'w')
       f.write(lastm)
       f.close()

       shutil.copytree('sample/img', 'output/img')
       shutil.copytree('sample/js', 'output/js')

       return render_template("index.html")

@app.route('/color', methods=['POST'])
def color():
    if request.method == 'POST':
        global color
        value = request.form['color']
        color = str(value)
        return '', 204
     
@app.route('/option', methods=['POST'])
def option():
    if request.method == 'POST':
        global imgpath
        global color
        color = '#5bc0de'
        isthisFile=request.files.get('file')
        isthisFile.save("./file/main.jpg")
        imgpath = './file/' + isthisFile.filename
        return jsonify({'file': 'true'})
    
if __name__ == '__main__':
    app.run(port=5000)
