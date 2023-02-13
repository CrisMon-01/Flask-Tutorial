from flask import Flask, redirect, url_for, render_template, request
from flask import session
from flask import flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key="RANDOM"
app.permanent_session_lifetime = timedelta(minutes=1)
  
@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nome_1']
        session['user'] = user
        flash("LOGIN OK!")
        return redirect(url_for('user'))
    else:
        if "user" in session:
            flash("YOU ALREADY LOGGED IN!")
            return render_template("user.html")

        return render_template("loginwithflash.html")


# uso session
@app.route("/user")
def user():
    if 'user' in session:
        user = session['user']
        return render_template("user.html", user= user)
    else:
        if'user' in session:
            return redirect(url_for('user'))
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    if 'user' in session:
        user = session['user']
        flash(f"USER: {user} LOGGED OUT ", "info")
        session.pop('user', None) 

    return(redirect(url_for("login")))

if __name__ == "__main__":
    app.run(debug=True) 