import os
from pathlib import Path
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, PasswordField, SubmitField

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()

load_dotenv(DOTENV_PATH)

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')

app = Flask(__name__)
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app.secret_key = APP_SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def user_login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
