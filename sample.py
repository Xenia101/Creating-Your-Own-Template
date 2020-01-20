from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def getuser():
   if request.method == 'POST':
      result = request.form
      print(result['Title'])
      print(result['Name'])
      return render_template("index.html",result = result)

if __name__ == '__main__':
    app.run(port=5000)
