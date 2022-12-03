from random import randint, choice
from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.width(3)
t.speed(10)
w = Screen()
w.colormode(255)

lim = 100


def generate_random_color():
    red = randint(0, 180)
    green = randint(0, 180)
    blue = randint(0, 180)
    return (red, green, blue)


def draw_bowndary(t):
    t.pu()
    t.setpos(-lim, lim)
    t.pd()
    for _ in range(4):
        t.forward(lim*2)
        t.right(90)
    t.pu()
    t.setpos(-(lim-20), -(lim-20))
    t.pd()


draw_bowndary(t)

t.dot(10, generate_random_color())
while t.pos()[1] <= 90:
    if t.pos()[0] > lim-30:
        t.pu()
        t.setpos(-(lim-20), t.pos()[1]+20)
        t.pd()
    else:
        t.pu()
        t.forward(20)
        t.pd()
    t.dot(10, generate_random_color())
w.exitonclick()
