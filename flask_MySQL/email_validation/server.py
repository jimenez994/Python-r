from flask import Flask, render_template,request,redirect,session,flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "Real Madrid"
mysql = MySQLConnector(app, 'emails_db')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
query = "select email, DATE_FORMAT(created_at, '%M, %e, %Y,%l:%i %p') AS date from email_table;"
Emails = mysql.query_db("select email, DATE_FORMAT(created_at, '%M, %e, %Y, %l:%i %p') AS date from email_table;")
print Emails
@app.route('/')
def index():
    
    return render_template("index.html")
@app.route('/validation',methods=["POST"])
def validation():
    errors = []
    
    if len(request.form["email"]) < 1:
        errors.append("Email cannot be blank")
        
    elif not EMAIL_REGEX.match(request.form["email"]):
        errors.append("Invalid email")
        
    if errors == []:

        query = "INSERT INTO email_table (email, created_at,updated_at) VALUES (:email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'email': request.form['email']     
            }
        mysql.query_db(query,data)
        
    for error in errors:
        flash(error)
    return redirect('/')

@app.route('/success')
def success():
    success = []
    
    success.append("The email address you entered is Valid")
    query = "select email, DATE_FORMAT(created_at, '%M, %e, %Y,%l:%i %p') AS date from email_table;"
    Emails = mysql.query_db("select email, DATE_FORMAT(created_at, '%M, %e, %Y, %l:%i %p') AS date from email_table;")

    for succ in success:
        flash(succ)
    return render_template("success.html", emails=Emails)
    




app.run(debug=True)
