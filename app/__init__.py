import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Cyber Sapiens", url=os.getenv("URL"))


@app.route("/about")
def about_us():
    return render_template("about.html")
