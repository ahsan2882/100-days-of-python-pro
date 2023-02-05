import time
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# python decorators

def delay_decorator(function):
    def wrapper_function():
        # do something before
        time.sleep(2)
        function()
        # do something after
        print("D")
    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def say_bye():
    print("bye")


say_hello()
