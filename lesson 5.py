from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  html=f"""
 <!doctype html>
 <html>
 <head>
      <title>My Styled Page</title>
      <link rel ="stylesheet" type ="text/css" href="/Static/css/style.css"
      </head>
      <body>
      <h1>This Should Look nice.</h1>
      <p> Click the link below To Navigate </p>
      <p>all Made With Flask</p>
      <img src = "/static/images/Flask_logo.svg" alt= "Flask logo">
      </body>
      </html>
    return html
    
app.run(Debug-True, Port = 5000)"""