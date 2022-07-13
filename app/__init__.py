import os
from flask import Flask, render_template, request, json
from dotenv import load_dotenv
import json
import requests
from flask_cors import cross_origin, CORS
from peewee import *
from playhouse.shortcuts import model_to_dict
import datetime
from flask import Response

load_dotenv()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1/"}})

# mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
#                       user=os.getenv("MYSQL_USER"),
#                       password=os.getenv("MYSQL_PASSWORD"),
#                       host=os.getenv("MYSQL_HOST"),
#                       port=3306
#                       )
# print(mydb)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared',uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

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


phobbies_file = open("app/static/data/phobbies.json")
phobbies = json.load(phobbies_file)

@app.route("/")
def index():
    return render_template("index.html", url=os.getenv("URL"))


@app.route("/mytimeline")
def mytimeline():
    return render_template("mytimeline.html", mytimeline_profiles=profile)


@app.route("/mytimeline/Roa/pro")
def rexperience():
    return render_template("rexp.html", rexperience=experience, redu=education)


@app.route("/mytimeline/Pedro/pro")
def experiencep():
    return render_template("pexp.html", pexperience=pexperience, pedu=peducation)


@app.route("/mytimeline/Roa/hobbies")
def hobbiesr():
    return render_template("rhobbies.html", rhobbies=rhobbies)

@app.route("/mytimeline/Pedro/hobbies")
def hobbiesp():
    return render_template("phobbies.html", phobbies=phobbies)

# Maps Section
@app.route("/maps")
def map():
    return render_template("maps.html", apikey=os.getenv("mapkey"))



@app.route("/api/timeline_post", methods=['POST'])
@cross_origin()
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    
    # ADDING TEST PORTION
    # . . . INCOMPLETE

    timeline_post = TimelinePost.create(
        name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route("/timeline")
def timeline():
    timeline = get_time_line_post()["timeline_posts"]
    return render_template('timeline.html', title="Timeline", url=os.getenv("URL"), timeline=timeline)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
