import flask
import random
from flask import request,jsonify

app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/api')
def page():
    return "API for collecting datasets"

data=[
    {
        'temparture':36.7,
        'pressure':110/40,
        'glucose':150,
        'heartrate':80,
        'oxygensaturation':96,
        'electrocardiogram':150,
    },
    {
        'temparture':40.1,
        'pressure':130/40,
        'glucose':250,
        'heartrate':50,
        'oxygensaturation':94,
        'electrocardiogram':170,
    },
    {
        'temparture':50.1,
        'pressure':150/40,
        'glucose':400,
        'heartrate':90,
        'oxygensaturation':105,
        'electrocardiogram':215,
    },
    {
        'temparture':35.1,
        'pressure':120/40,
        'glucose':300,
        'heartrate':98,
        'oxygensaturation':92,
        'electrocardiogram':150,
    },
]

@app.route('/api/datasets',methods=['GET'])
def datasets():
    if request.method=="GET": 
        return jsonify(data[0:2]) 
app.run()