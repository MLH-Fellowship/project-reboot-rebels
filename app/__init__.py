import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)
data_file = open('app/static/data/profile.json')
data = json.load(data_file)


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', timeline_profiles=data)


@app.route("/")
def index():
    return render_template("index.html", title="Cyber Sapiens", url=os.getenv("URL"))


@app.route("/about")
def about_us():
    return render_template("about.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0") 
