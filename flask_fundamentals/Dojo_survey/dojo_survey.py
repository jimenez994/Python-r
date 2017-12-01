from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/info', methods=["POST"])
def process():
    name = request.form['name']
    last = request.form['last']
    location = request.form['location']
    language = request.form['fav_language']
    comment_field = request.form['comment_field']
    
    print name
    return render_template('info.html', first_name=name, last_name=last,fav_location=location,fav_language=language,comment_field=comment_field)





app.run(debug=True)
