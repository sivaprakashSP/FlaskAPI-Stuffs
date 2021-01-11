import flask
from flask import request,jsonify

app=flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/sum')
def home():
    return "<h1>5 is the sum</h1>"

app.run()