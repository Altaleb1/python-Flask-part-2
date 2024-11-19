from flask import Flask

app = Flask(__name__)

##Homepage
@app.route("/")
def home():
  html="""
  h1>Welcome to my homepage</h1>
  <p> Click the link below To Navigate </p>
  <a>href="/about". Go To About Us Page</a>
  """
  return html 
  ###About Page
  @app.route("/about")
  def about():
              html="""
  h1>Welcome to my about page</h1>
  <p> I'm an epic coder </p>
  <a>href="/about". Go To  HomePage</a>
  """

              return html 
app.run(Debug=True, Port = 5000)