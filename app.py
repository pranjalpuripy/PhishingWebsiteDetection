from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import joblib
from database.db import create_database

app = Flask(__name__)

create_database()

model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

import sqlite3
from flask import request, redirect

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database/database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(fullname,email,password) VALUES(?,?,?)",
            (fullname, email, password)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/scan", methods=["GET", "POST"])
def scan():

    if request.method == "POST":

        url = request.form["url"]

        url_vector = vectorizer.transform([url])

        prediction = model.predict(url_vector)[0]

        if prediction == 0:
            result = "SAFE WEBSITE ✅"
            image = "shield.png"
        else:
            result = "PHISHING WEBSITE ⚠️"
            image = "warning.png"

        return render_template(
            "result.html",
            website=url,
            prediction=result,
            image=image
        )

    return render_template("scan.html")


@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/history")
def history():
    return render_template("history.html")

if __name__ == "__main__":
    create_database()
    app.run(debug=True)

