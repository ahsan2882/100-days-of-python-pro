import os
# import sqlite3
from pathlib import Path
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask import Flask, render_template, request, redirect, url_for

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()

load_dotenv(DOTENV_PATH)
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')


DB_FILE_PATH = Path(
    Path(__file__).parent.resolve(), 'books-collection.db'
).resolve()

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
bootstrap = Bootstrap5(app)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_FILE_PATH}"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


def validate_rating(form, field):
    if int(float(field.data)) not in range(1, 11):
        raise ValidationError('Rating must be between 1 and 10')


class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[
                         DataRequired(), validate_rating])
    submit = SubmitField('Submit')


class EditRating(FlaskForm):
    rating = StringField('New Rating', validators=[
                         DataRequired(), validate_rating])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = AddBookForm()
    if form.validate_on_submit() and request.method.upper() == 'POST':
        new_book = Book(title=form.title.data,
                        author=form.author.data, rating=float(form.rating.data))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route('/edit/<int:book_id>', methods=['POST', 'GET'])
def edit_rating(book_id):
    form = EditRating()
    book = db.session.query(Book).get(book_id)
    if form.validate_on_submit() and request.method.upper() == 'POST':
        book.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book, form=form)


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = db.session.query(Book).get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
