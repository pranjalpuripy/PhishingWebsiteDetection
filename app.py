from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import joblib

from database.db import create_database


# =========================================================
# FLASK APPLICATION
# =========================================================

app = Flask(__name__)

app.secret_key = "cybershield_ai_secret_key_2026"


# =========================================================
# CREATE DATABASE
# =========================================================

create_database()


# =========================================================
# LOAD AI MODEL
# =========================================================

model = joblib.load("model/phishing_model.pkl")

vectorizer = joblib.load("model/vectorizer.pkl")


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# ABOUT PAGE
# =========================================================

@app.route("/about")
def about():

    # Check login

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("about.html")


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]


        # Connect to database

        conn = sqlite3.connect("database/database.db")

        cursor = conn.cursor()


        # Check user credentials

        cursor.execute("""
            SELECT id, fullname, email
            FROM users
            WHERE email = ? AND password = ?
        """, (email, password))


        user = cursor.fetchone()


        conn.close()


        # =================================================
        # LOGIN SUCCESS
        # =================================================

        if user:

            session["user_id"] = user[0]
            session["fullname"] = user[1]
            session["email"] = user[2]

            return redirect(url_for("dashboard"))


        # =================================================
        # LOGIN FAILED
        # =================================================

        return render_template(
            "login.html",
            error="Invalid email or password."
        )


    return render_template("login.html")


# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]

        email = request.form["email"]

        password = request.form["password"]


        # Connect to database

        conn = sqlite3.connect("database/database.db")

        cursor = conn.cursor()


        # Insert new user

        cursor.execute(
            """
            INSERT INTO users(fullname, email, password)
            VALUES(?, ?, ?)
            """,
            (fullname, email, password)
        )


        conn.commit()

        conn.close()


        # Redirect to login

        return redirect(url_for("login"))


    return render_template("register.html")


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    # =====================================================
    # CHECK LOGIN
    # =====================================================

    if "user_id" not in session:
        return redirect(url_for("login"))


    # Connect to database

    conn = sqlite3.connect("database/database.db")

    cursor = conn.cursor()


    # =====================================================
    # TOTAL SCANS
    # =====================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM scan_history
    """)

    total_scans = cursor.fetchone()[0]


    # =====================================================
    # SAFE WEBSITES
    # =====================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM scan_history
        WHERE result = 'SAFE'
    """)

    safe_scans = cursor.fetchone()[0]


    # =====================================================
    # PHISHING WEBSITES
    # =====================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM scan_history
        WHERE result = 'PHISHING'
    """)

    phishing_scans = cursor.fetchone()[0]


    # =====================================================
    # TODAY'S SCANS
    # =====================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM scan_history
        WHERE DATE(scan_date) = DATE('now', 'localtime')
    """)

    today_scans = cursor.fetchone()[0]


    # =====================================================
    # RECENT SCANS
    # =====================================================

    cursor.execute("""
        SELECT website, result, scan_date
        FROM scan_history
        ORDER BY id DESC
        LIMIT 5
    """)

    recent_scans = cursor.fetchall()


    # =====================================================
    # CLOSE DATABASE
    # =====================================================

    conn.close()


    # =====================================================
    # SEND DATA TO DASHBOARD
    # =====================================================

    return render_template(
        "dashboard.html",
        total_scans=total_scans,
        safe_scans=safe_scans,
        phishing_scans=phishing_scans,
        today_scans=today_scans,
        recent_scans=recent_scans
    )


# =========================================================
# SCAN WEBSITE
# =========================================================

@app.route("/scan", methods=["GET", "POST"])
def scan():

    # =====================================================
    # CHECK LOGIN
    # =====================================================

    if "user_id" not in session:
        return redirect(url_for("login"))


    if request.method == "POST":

        # Get URL entered by user

        url = request.form["url"]


        # Convert URL into vector

        url_vector = vectorizer.transform([url])


        # Predict using AI model

        prediction = model.predict(url_vector)[0]


        # =================================================
        # DETERMINE RESULT
        # =================================================

        if prediction == 0:

            result = "SAFE WEBSITE ✅"

            database_result = "SAFE"

            image = "shield.png"

        else:

            result = "PHISHING WEBSITE ⚠️"

            database_result = "PHISHING"

            image = "warning.png"


        # =================================================
        # SAVE SCAN RESULT TO DATABASE
        # =================================================

        conn = sqlite3.connect("database/database.db")

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO scan_history (website, result)
            VALUES (?, ?)
            """,
            (url, database_result)
        )


        conn.commit()

        conn.close()


        # =================================================
        # DISPLAY RESULT PAGE
        # =================================================

        return render_template(
            "result.html",
            website=url,
            prediction=result,
            image=image
        )


    return render_template("scan.html")


# =========================================================
# RESULT PAGE
# =========================================================

@app.route("/result")
def result():

    # Check login

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("result.html")


# =========================================================
# HISTORY PAGE
# =========================================================

@app.route("/history")
def history():

    # =====================================================
    # CHECK LOGIN
    # =====================================================

    if "user_id" not in session:
        return redirect(url_for("login"))


    # Connect to database

    conn = sqlite3.connect("database/database.db")

    cursor = conn.cursor()


    # Fetch all scan history

    cursor.execute("""
        SELECT id, website, result, scan_date
        FROM scan_history
        ORDER BY id DESC
    """)


    scans = cursor.fetchall()


    # Close database connection

    conn.close()


    # Send scan data to history.html

    return render_template(
        "history.html",
        scans=scans
    )


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    # Clear login session

    session.clear()


    # Go back to login page

    return redirect(url_for("login"))


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    create_database()

    app.run(debug=True)