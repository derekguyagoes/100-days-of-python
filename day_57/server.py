import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_gender(name):
    response = requests.get("https://api.genderize.io/?name={}".format(name))
    return response.json()["gender"]


def get_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()["age"]


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", random_number=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
