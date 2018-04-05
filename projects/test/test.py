# -*- coding: utf-8 -*-
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    CAT = u'''
    .                     ________________________
              ∧ ∧　  /
        〜′‾‾( ﾟДﾟ) < {}
          UU‾‾U U　  \________________________
    '''
    time = datetime.now().strftime("%I:%M %p")

    return CAT.format("The time is: {}".format(time))

app.run(debug=True)

