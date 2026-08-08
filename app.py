from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

if not os.path.exists("database/employee.db"):
    os.system("python init_db.py")

app = Flask(__name__)

app.secret_key = "LEGACY_PORTAL"

DATABASE = "database/employee.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = get_db_connection()

    # ---------- INTENTIONAL VULNERABILITY ----------
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    # -----------------------------------------------

    try:
        user = conn.execute(query).fetchone()

    except sqlite3.Error:

        conn.close()

        return render_template(
            "login.html",
            error="Authentication failed."
        )

    conn.close()

    if user:

        session["username"] = user["username"]
        session["role"] = user["role"]

        if user["role"] == "admin":
            return redirect("/admin")

        return redirect("/dashboard")

    return render_template(
        "login.html",
        error="Invalid username or password."
    )


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


@app.route("/admin")
def admin():

    if "username" not in session:
        return redirect("/")

    if session["role"] != "admin":
        return render_template("error.html"), 403

    with open("flag.txt", "r") as f:
        flag = f.read().strip()

    return render_template(
        "admin.html",
        username=session["username"],
        flag=flag
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )