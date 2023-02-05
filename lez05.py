from flask import Flask, redirect, url_for, render_template, request
from flask import session
from datetime import timedelta

app = Flask(__name__)

#info su session sono criptate
app.secret_key="RANDOM"
#permanent session
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        # user = request.form['nome_1']
        # #session
        # session['user'] = user
        #permanent
        session.permanent = True
        user = request.form['nome_1']
        #session
        session['user'] = user
        return redirect(url_for('user'))
    else:
        return render_template("form.html")

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"

# uso session
@app.route("/user")
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"
    else:
        if'user' in session:
            return redirect(url_for('user'))
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('user', None) #pulisco la sessione
    return(redirect(url_for("login")))

if __name__ == "__main__":
    app.run(debug=True) 