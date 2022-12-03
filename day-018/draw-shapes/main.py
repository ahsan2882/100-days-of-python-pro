from turtle import Turtle, Screen
from random import randint

win = Screen()
win.canvwidth = 1000
win.canvheight = 1000
win.colormode(255)


def generate_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def draw_shape(sides, t):
    angle = 360 / sides
    shape_color = generate_random_color()
    print(shape_color)
    t.color(shape_color)
    for _ in range(sides):
        t.forward(100)
        t.right(angle)


t = Turtle()
t.shape("turtle")
t.penup()
t.setpos(0, 300)
t.pendown()

for sides in range(3, 11):
    draw_shape(sides, t)


win.exitonclick()
