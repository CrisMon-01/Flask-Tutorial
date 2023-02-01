from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/idx/<name>")
def content(name):
    return render_template("index1.html", content1=name, content2="test")

@app.route("/var")
def pythoninhtml():
    return render_template("index2.html")

@app.route("/list")
def listhtml():
    return render_template("index3.html", contents=['A','B','C'])



if __name__ == "__main__":
    app.run()