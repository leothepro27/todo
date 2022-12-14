#import libraries
import os
from cs50 import SQL
from flask import Flask, render_template
from flask_session import Session

#Create app with Flask:
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session:
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#return HTML code from file
@app.route("/")
def index():
    return render_template("index.html")


