from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="index")

@app.route('/chai')
def chai():
    return render_template("chai.html", title="hello")

@app.route('/hello')
def hello():
    return 'hello'
