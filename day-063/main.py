import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask import Flask, render_template, request, redirect, url_for

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()

load_dotenv(DOTENV_PATH)
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')


app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
bootstrap = Bootstrap5(app)


all_books = []


def validate_rating(form, field):
    if int(field.data) not in range(1, 11):
        raise ValidationError('Rating must be between 1 and 10')


class LibraryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[
                         DataRequired(), validate_rating])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = LibraryForm()
    if form.validate_on_submit() and request.method.upper() == 'POST':
        new_book = {
            "title": form.title.data,
            "author": form.author.data,
            "rating": int(form.rating.data)
        }
        all_books.append(new_book)
        print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
