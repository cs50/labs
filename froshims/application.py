from flask import Flask, render_template, request
import csv

# Configure applicdation
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("email") or not request.form.get("dorm"):
        return render_template("failure.html")
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("email"), request.form.get("dorm")))
    file.close()
    return render_template("success.html")


@app.route("/registered")
def registered():
    file = open("registered.csv", "r")
    reader = csv.reader(file)
    students = list(reader)
    file.close()
    return render_template("registered.html", students=students)
