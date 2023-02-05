from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def home():
    return """<h1 style='text-align:center; margin-bottom:2rem;'>Guess a number from 0 to 9</h1>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style='display:block;margin-left:auto;margin-right:auto;width:50%'>
"""


guess_number = randint(0, 9)


@app.route('/<int:number>')
def guess(number):
    if number > guess_number:
        return """<h1 style='text-align:center; margin-bottom:2rem;'>Too high, try again!</h1>
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>
    """
    elif number < guess_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    # run the app in debug mode
    app.run(debug=True)
