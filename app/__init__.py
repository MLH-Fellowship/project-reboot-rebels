import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)
profile_file = open("app/static/data/profile.json")
profile = json.load(profile_file)

experience_file = open("app/static/data/exp.json")
experience = json.load(experience_file)

education_file = open("app/static/data/edu.json")
education = json.load(education_file)

pexperience_file = open("app/static/data/pexp.json")
pexperience = json.load(pexperience_file)

peducation_file = open("app/static/data/pedu.json")
peducation = json.load(peducation_file)

rhobbies_file = open("app/static/data/hobbies.json")
rhobbies = json.load(rhobbies_file)


@app.route("/")
def index():
    return render_template("index.html", title="Cyber Sapiens", url=os.getenv("URL"))


@app.route("/timeline")
def timeline():
    return render_template("timeline.html", timeline_profiles=profile)


@app.route("/timeline/Roa/pro")
def rexperience():
    return render_template("rexp.html", rexperience=experience, redu=education)


@app.route("/timeline/Pedro/pro")
def experiencep():
    return render_template("pexp.html", pexperience=pexperience, pedu=peducation)


@app.route("/timeline/Roa/hobbies")
def hobbiesr():
    return render_template("rhobbies.html", rhobbies=rhobbies)


# Maps Section
@app.route("/maps")
def map():
    return render_template("maps.html", apikey=os.getenv("mapkey"))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
