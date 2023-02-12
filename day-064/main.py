
import os
import sqlite3
import requests
from pathlib import Path
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from flask import Flask, render_template, request, redirect, url_for
from wtforms.validators import DataRequired, ValidationError, length


DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()

load_dotenv(DOTENV_PATH)
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')


DB_FILE_PATH = Path(
    Path(__file__).parent.resolve(), 'movies-collection.db'
).resolve()

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
bootstrap = Bootstrap5(app)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE_PATH}"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


def validate_rating(form, field):
    if int(float(field.data)) not in range(1, 11):
        raise ValidationError('Rating must be between 1 and 10')


class AddMovie(FlaskForm):
    title = StringField('Movie', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditRatingForm(FlaskForm):
    rating = StringField('New Rating', validators=[
                         DataRequired(), validate_rating])
    review = StringField('New Review', validators=[
                         DataRequired(), length(min=15)])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit_review(movie_id):
    form = EditRatingForm()
    movie = Movie.query.get(movie_id)
    if request.method.upper() == "POST" and form.validate_on_submit():
        movie.review = form.review.data
        movie.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit() and request.method.upper() == "POST":
        movie_title = form.title.data
        response = requests.get(
            f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}")
        data = response.json()["results"]
        # print(data)
        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)


@app.route('/find/<int:movie_id>')
def find_movie(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}", params={"api_key": TMDB_API_KEY, "language": "en-US"})
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        rating=data["vote_average"],
        ranking=1,
        review="My favourite character was the caller.",
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit_review', movie_id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
