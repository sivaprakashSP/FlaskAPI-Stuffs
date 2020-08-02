import flask

app=flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/sum')
def home():
    return "<h1>5 is the sum</h1>"

app.run(host='0.0.0.0')