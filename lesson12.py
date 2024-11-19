from flask import Flask, render_template , request
import sqlite3

app = Flask(__name__)
@app.route("/add",methods =("Get","Post"))
def AddStudent():
            #Did The user post data?
            if request.method == "POST":
                    
                    #Get The Names from the form
                    firstname= request.form['firstnname']
                    lastname = request.form['lastname']
                    dob = request.form['dob']

                    #Build our query and save to the databse
                    db = sqlite3.connect("databse/student_marks.db")
                    db.execute("INSERT into students ('firstname' , 'lastname' , 'dob') VALUES(?,?,?)",
                               firstname, lastname, dob)
                    db.commit()
                    db.close()

                    return render_template("add.html")

app.run(debug = True, port = 5000)