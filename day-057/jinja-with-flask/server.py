import requests
from random import randint
from datetime import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    randomNumber = randint(1, 10)
    year = dt.now().year
    return render_template('index.html', randomNumber=randomNumber, year=year)


@app.route('/guess/<name>')
def guessAgeAndGender(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(
        f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template('guess.html', name=name.title(), gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
