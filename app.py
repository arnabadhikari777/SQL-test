import os

from flask import Flask, redirect, render_template, request
import mysql.connector

app = Flask(__name__)


def get_database():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "Dhruba@1234"),
        database=os.environ.get("MYSQL_DATABASE", "python_link"),
    )


@app.route("/")
def home():
    db = get_database()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM demo")
        users = cursor.fetchall()
    finally:
        cursor.close()
        db.close()

    return render_template("index.html", users=users)


@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")

    name = request.form["name"]
    email = request.form["email"]

    db = get_database()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT COALESCE(MAX(id), 0) FROM demo")
        new_id = cursor.fetchone()[0] + 1

        cursor.execute(
            "INSERT INTO demo (id, name, email) VALUES (%s, %s, %s)",
            (new_id, name, email),
        )
        db.commit()
    finally:
        cursor.close()
        db.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
