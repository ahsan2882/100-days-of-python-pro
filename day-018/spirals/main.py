from turtle import Turtle, Screen
from random import randint

t = Turtle()
t.width(2)
t.speed(10)
w = Screen()
w.colormode(255)


def generate_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def draw_circle(t):
    t.color(generate_random_color())
    t.circle(100, 360)


def draw_spirograph(size_of_gap, t):
    size = size_of_gap
    for _ in range(int(360/size_of_gap)):
        t.setheading(size)
        draw_circle(t)
        size += size_of_gap


draw_spirograph(10, t)


w.exitonclick()
