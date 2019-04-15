from flask import Flask, render_template, redirect, request
from cs50 import SQL
import random

app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///quotes.db")

@app.route("/")
def index():
    """ This page will be the main page where you guess quotes """

    rows = db.execute("SELECT * FROM quotes")
    num = random.randrange(0, len(rows))
    return render_template("index.html", quote=rows[num]["string"], number=encode(rows[num]["name"]), name=rows[num]["name"])


@app.route("/entry", methods=["GET", "POST"])
def entry():
    """ This page allows you to insert new quotes into the database """

    if request.method == "POST":
        # add quotes to databases
        db.execute("INSERT INTO quotes (string, name) VALUES (:string, :name)", string=request.form.get("qt"), name=request.form.get("name"))
        return redirect("/entry")
    else:
        return render_template("entry.html")


@app.route("/view")
def view():
    """ This page will be the main page where you guess quotes """

    rows = db.execute("SELECT * FROM quotes ")
    return render_template("view.html", rows=rows)


def encode(name):
    """ This function turns names into a set number code """

    num = 0
    if name == "Nicholas Andrysiak":
        num = 1
    elif name == "Josh Cowden":
        num = 2
    elif name == "Alex Dosch":
        num = 3
    elif name == "Jacob Frabutt":
        num = 4
    elif name == "Bridget Goodwine":
        num = 5
    elif name == "Emily Hall":
        num = 6
    elif name == "Jonathan Liu":
        num = 7
    elif name == "Adam Mazurek":
        num = 8
    elif name == "Jacob Moon":
        num = 9
    elif name == "Andrew Orians":
        num = 10
    elif name == "Rebecca Pan":
        num = 11
    elif name == "Elena Parial":
        num = 12
    elif name == "Linh Phan":
        num = 13
    elif name == "Bill Powers":
        num = 14
    elif name == "Tomás Aguilar-Fraga":
        num = 15
    elif name == "Mr. Wojtowicz":
        num = 16
    return num