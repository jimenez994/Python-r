from flask import Flask , render_template,request, redirect,session,flash
# import the connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "real madrid"
# connect and store the connection in "mysql";note that you pass the database name to the function
mysql = MySQLConnector(app,'full_friends')
@app.route("/")
def index():
    query = "select name, age, DATE_FORMAT(created_at, '%M, %e, %Y') AS date from friends;"
    friends = mysql.query_db("select name, age, DATE_FORMAT(created_at, '%M, %e, %Y') AS date from friends;")
    print friends
    return render_template("index.html", all_friends=friends)

@app.route("/add", methods=['POST'])
def create():
    errors = []
    if len(request.form['name']) < 5:
        errors.append("hey! I need your full name to be my friend")
    if len(request.form['age']) < 2:
        errors.append("You must be older to be my friend")
    
    if errors == []:
        query = "INSERT INTO friends (name, age, created_at,updated_at) VALUES (:name, :age, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'name': request.form['name'],
                'age':  request.form['age'],
                
            }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)

        return redirect('/')
    for error in errors:
        flash (error)
    return redirect('/')








app.run(debug=True)

