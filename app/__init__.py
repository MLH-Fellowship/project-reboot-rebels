import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from data import profiles

load_dotenv()
app = Flask(__name__)


@app.route("/timeline")
def timeline():
    return render_template("timeline.html", timeline_profiles=profiles)


@app.route("/")
def index():
    return render_template("index.html", title="Cyber Sapiens", url=os.getenv("URL"))


@app.route("/about")
def about_us():
    return render_template("about.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
