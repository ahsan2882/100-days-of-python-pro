import os
import csv
from pathlib import Path
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from wtforms.validators import DataRequired,ValidationError
from wtforms import StringField, SubmitField,SelectField

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()

CAFE_DATA_PATH= Path(
    Path(__file__).parent.resolve(), 'cafe-data.csv'
).resolve()

load_dotenv(DOTENV_PATH)

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
bootstrap = Bootstrap5(app)


def validate_URL(form, field):
    if not field.data.startswith('https://goo.gl/maps/'):
        raise ValidationError('URL is not a map location URL.')


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), validate_URL])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating',choices=[(0,'✘'),(1,'☕️'),(2,'☕️☕️'),(3,'☕️☕️☕️'),(4,'☕️☕️☕️☕️'),(5,'☕️☕️☕️☕️☕️')], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating',choices=[(0,'✘'),(1,'💪'),(2,'💪💪'),(3,'💪💪💪'),(4,'💪💪💪💪'),(5,'💪💪💪💪💪')], validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability', choices=[(0,'✘'),(1,'🔌'),(2,'🔌🔌'),(3,'🔌🔌🔌'),(4,'🔌🔌🔌🔌'),(5,'🔌🔌🔌🔌🔌')],validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit() and request.method == 'POST':
        with open(CAFE_DATA_PATH, 'a', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([form.cafe.data, form.location.data, form.open_time.data, form.closing_time.data, form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data])
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(CAFE_DATA_PATH,encoding='utf-8', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
