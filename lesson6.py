#We need to import a new object for templates
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    #Return to the page found at templates/index.html
    return render_template('index.html')
app.run(Debug=True, port = 5000)