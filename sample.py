from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'C:\\Users\\User\\Desktop\\Creating-Your-Own-Template\\file'
app.secret_key = "XENIA"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def getuser():
   if request.method == 'POST':
      result = request.form
      
      print(result)
      return render_template("index.html",result = result)

@app.route('/option', methods=['POST'])
def option():
    if request.method == 'POST':
        isthisFile=request.files.get('file')
        isthisFile.save("./file/"+isthisFile.filename)
        return jsonify({'file': 'true'})
    
if __name__ == '__main__':
    app.run(port=5000)
