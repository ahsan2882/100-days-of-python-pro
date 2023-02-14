import os
from pathlib import Path
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, PasswordField
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, session, request, url_for, redirect, flash, send_from_directory
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


def define_path(filename: str):
    return Path(
        Path(__file__).parent.resolve(),
        filename
    ).resolve()


DOTENV_PATH = define_path(".env")
DB_PATH = define_path("users.db")

load_dotenv(DOTENV_PATH)

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

db = SQLAlchemy()
app = Flask(__name__)

app.secret_key = APP_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap5(app)
app.app_context().push()

db.init_app(app)


# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.create_all()


class RegisterForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label='Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Me Up!')


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method.upper() == "POST" and form.validate_on_submit():
        user_name = form.name.data
        user_email = form.email.data
        user_password = form.password.data

        new_user = User(name=user_name, email=user_email,
                        password=user_password)
        db.session.add(new_user)
        db.session.commit()
        session['user_name'] = user_name
        return redirect(url_for('secrets'))
    return render_template("register.html", form=form)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html", name=session['user_name'])


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
