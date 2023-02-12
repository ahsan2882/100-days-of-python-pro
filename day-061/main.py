import os
from pathlib import Path
from dotenv import load_dotenv
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, render_template

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()

load_dotenv(DOTENV_PATH)

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')


app.secret_key = APP_SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def user_login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
