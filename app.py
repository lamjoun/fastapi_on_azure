# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! This is a Flask App deployed on Azure Web App.'

@app.route('/tt')
def hellott():
    return '====== Hello World! This is a Flask App deployed on Azure Web App.==tt'

if __name__ == '__main__':
    app.run(debug=True)
