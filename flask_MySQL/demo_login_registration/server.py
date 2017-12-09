from flask import Flask, render_template, redirect,request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'users_db')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    errors = []
    if len(request.form['first']) < 1:
        errors.append("must contain a name")
    elif len(request.form['first']) < 2:
        errors.append("must be longer")
    if len(request.form['last']) < 1:
        errors.append("must contain a las name")
    elif len(request.form['last']) < 2:
        errors.append("must be longer")
    if len(request.form['email']) < 1:
        errors.append("must contain a email")
    if len(request.form['password']) < 1:
        errors.append("must contain a password")
    elif len(request.form['password']) < 7:
        errors.append("must be longer")
    if len(request.form['pass_confirm']) < 1:
        errors.append("not match")
    elif request.form['pass_confim'] != request.form['password']:
        errors.append('must match')
    print errors
    print request.form

    return redirect("/")

app.run(debug=True)
