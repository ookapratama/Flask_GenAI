from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
def tes() :
   return "Hello World"

@app.route('/')
def index() :
   tes = 'nama'
   return render_template('index.html', tes=tes)

if __name__ == '__main__' :
   app.run()