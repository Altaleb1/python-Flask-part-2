from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    #Set a variable to a value
    namevalue="Bob"
    timeValue= datetime.now().strftime("%y-%m-%d %H:%M:%S")
    #Set The template to our variable 
    return render_template('index.html',name=namevalue, time =timeValue)
app.run(Debug=True, port = 5000)