from turtle import Turtle, Screen
from random import choice, randint

lim = 360


def generate_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def draw_boundary():
    t.pu()
    t.setpos(-lim, lim)
    t.pd()
    for _ in range(4):
        t.forward(lim*2)
        t.right(90)
    t.pu()
    t.setpos(0, 0)
    t.pd()


t = Turtle()
t.shape("turtle")
thickness = 1
t.speed(10)

screen = Screen()
screen.colormode(255)
prev_dir = None

draw_boundary()

for i in range(5000):
    if thickness < 15:
        thickness += 0.02
    t.width(thickness)
    t.color(generate_random_color())
    while True:
        new_dir = choice(range(0, 360, 90))
        if prev_dir is not None:
            if new_dir != prev_dir and new_dir != 180:
                break
        else:
            prev_dir = new_dir
    prev_dir = new_dir
    t_pos = t.pos()
    if (t_pos[0] > (lim-20) or t_pos[0] < -(lim-20) or
            t_pos[1] > (lim-20) or t_pos[1] < -(lim-20)):
        t.left(90)
        t.forward(20)
    else:
        t.right(new_dir)
        t.forward(20)

screen.exitonclick()
