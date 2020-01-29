from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\User\\Desktop\\Creating-Your-Own-Template\\file'
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
       print(result)
       #print(color)
       #print(imgpath)
       
       msg = list()
       editlist = [result['Title'], str(color), str(color), result['Title'],str(color),
                   result['Name'], result['TEXT'], result['location'], result['email'],
                   str('https://github.com/')+result['GithubID'], result['facebook'], result['GithubID']
                   ]
       for x in range(1,14):
           filename = 'C:\\Users\\User\\Desktop\\Creating-Your-Own-Template\\index_gen\\' + str(x)
           f = open(filename, 'r')
           msg.append(f.read().replace('\n',''))
           f.close()

       print(len(msg))
       print(len(editlist))
       lastm = ''
       for x in range(12):
           m = msg[x] + editlist[x]
           lastm += m
       lastm += msg[-1]
       print(lastm)
           
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
        isthisFile.save("./file/"+isthisFile.filename)
        imgpath = './file/' + isthisFile.filename
        return jsonify({'file': 'true'})
    
if __name__ == '__main__':
    app.run(port=5000)
