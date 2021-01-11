import flask
import random
#from flask import request,jsonify
#import json 

app=flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/api')
def page():
    return "API for collecting datasets"

@app.route('/api/normal',methods=['GET'])
def normal():
    data={
        "temparture":random.randint(36,37),
        "pressure":random.randint(90,120),
        "respiration":random.randint(12,16),
        "glucose":random.randint(72,140),
        "heartrate":random.randint(60,100),
        "oxygenSaturation":random.randint(95,100),
        "cholestrol":random.randint(125,200)
    }
    return(data)

@app.route('/api/diabetes',methods=['GET'])
def diabetes():
    dataset={
        "temperature": random.randint(35, 37),
        "pressure": random.randint(90, 120),
        "respiration": random.randint(12, 16),
        "glucose": random.randint(72, 140),
        "heartRate": random.randint(60, 100),
        "oxygenSaturation": random.randint(50, 96),
        "cholesterol": random.randint(125, 200)
    }
    return(dataset)

@app.route('/api/prediabetes',methods=['GET'])
def prediabetes():
    dataset={
        "temperature": random.randint(36, 38),
        "pressure": random.randint(90, 120),
        "respiration": random.randint(12, 16),
        "glucose": random.randint(140,199),
        "heartRate": random.randint(60, 100),
        "oxygenSaturation": random.randint(95,100),
        "cholesterol": random.randint(125, 200)

    }
    return(dataset)

@app.route('/api/ModerateAcuteAsthma',methods=['GET'])
def ModerateAcuteAsthma():
    dataset={

        "Temperature": random.randint(35, 37),
        "Pressure": random.randint(90, 120),
        "respiration": random.randint(20, 30),
        "glucose": random.randint(72, 140),
        "heartRate": random.randint(100, 125),
        "oxygenSaturation": random.randint(92, 95),
        "cholesterol": random.randint(125, 200),
    }
    return(dataset)

@app.route('/api/Hypoxemia',methods=['GET'])
def hypoxemia():
    dataset={
        "Temperature": random.randint(35, 37),
        "Pressure": random.randint(90, 120),
        "respiration": random.randint(20, 30),
        "glucose": random.randint(72, 140),
        "heartRate": random.randint(100, 125),
        "oxygenSaturation": random.randint(92, 95),
        "cholesterol": random.randint(125, 200),
    }
    return(dataset)

@app.route('/api/Bronchiectasis',methods=['GET'])
def bronchiectasis():
    dataset={
        "Temperature": random.randint(35, 37),
        "Pressure": random.randint(90, 120),
        "respiration": random.randint(40, 60),
        "glucose": random.randint(72, 140),
        "heartRate": random.randint(60, 100),
        "oxygenSaturation": random.randint(95, 100),
        "cholesterol": random.randint(125, 200),
    }
    return(dataset)
app.run(debug=True)