from flask import Flask
from datetime import datetime

 #Create The flask App
app = Flask(__name__)
#Homepage Route
@app.route("/")
def home():
 #Get Now and format as  Year-Month-Day Hour:Minute:Second
     today = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    #Set up the page's html
     html = f"""
<!doctype html>
<html>
<head>
     <title>Clock</Title>
     </head>
     <body>
     <h1>Welcome to my clock</h1>
     <p> The current time and date is {today}</p>
     </body>
     </html>
     """
#return the html
     return html 
app.run(debug=True, Port = 5000)