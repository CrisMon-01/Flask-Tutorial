from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nome_1']
        return redirect(url_for('user', usr=user))
    else:
        return render_template("form.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True) 