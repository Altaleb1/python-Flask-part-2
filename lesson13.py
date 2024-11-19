from flask import Flask, request, render_template, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

@app.route("/add", methods=["GET", "POST"])
def AddStudent():
    # Did the user post data?
    if request.method == "POST":
        # Get the values from the form
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob = request.form['dob']

        # Connect to the database
        db = sqlite3.connect("database/student_marks.db")
        cursor = db.cursor()

        # Check if the student already exists
        cursor.execute("SELECT * FROM Students WHERE firstname = ? AND lastname = ? AND dob = ?", (firstname, lastname, dob))
        existing_student = cursor.fetchone()

        if existing_student:
            # Student exists, show a message
            flash(f"Student {firstname} {lastname} with DOB {dob} already exists.")
        else:
            # Student doesn't exist, insert the new record
            cursor.execute("INSERT INTO Students ('firstname', 'lastname', 'dob') VALUES (?, ?, ?)", (firstname, lastname, dob))
            db.commit()
            flash(f"Student {firstname} {lastname} added successfully.")

        db.close()

    return render_template("add.html")

    app.run(debug=True, port=5000)
