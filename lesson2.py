from flask import Flask

#Create the web host app
app = Flask(__name__)

#This route is for our homepage
@app.route("/")
def home():
  return"Hello, World"

#Start The web app
app.run(debug=True, Port=5000)