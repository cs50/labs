import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)
db = SQL("sqlite:///birthdays.db")


@app.route("/", methods=["GET", "POST"])
def index():
    # TODO: If the request method is GET, display the entries in the database. If the method is POST, add the entry into the database.
    return render_template("index.html")

