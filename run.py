from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates')

@app.route('/hello')
def tes() :
   return "Hello World"

@app.route('/')
def index() :
   # tes = 'nama'
   return render_template('index.html')

if __name__ == '__main__' :
   app.run(debug = True)