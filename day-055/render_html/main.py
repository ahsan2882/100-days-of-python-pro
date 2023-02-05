from flask import Flask
from style_decorators import make_bold, make_emphasis, make_underline

app = Flask(__name__)


@app.route('/')
def home():
    return """<h1 style='text-align:center'>Home Page</h1>
        <p style='text-align:center'>This is the home page</p>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style='display:block;margin-left:auto;margin-right:auto;width:50%'>
"""

# Different routes using the app.route decorator


@app.route('/bye')
@make_bold
@make_underline
@make_emphasis
def bye():
    return "Bye"

# Creating variable paths and converting the data type


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


if __name__ == "__main__":
    # run the app in debug mode
    app.run(debug=True)
