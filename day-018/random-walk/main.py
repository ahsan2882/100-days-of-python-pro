from turtle import Turtle, Screen
from random import choice, randint


def generate_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


t = Turtle()
t.shape("turtle")
thickness = 1
t.speed(10)

screen = Screen()
screen.colormode(255)
prev_dir = None

for i in range(5000):
    if thickness < 10:
        thickness += 0.2
    t.width(thickness)
    t.color(generate_random_color())
    while True:
        new_dir = choice(range(0, 360, 90))
        if prev_dir != None:
            if new_dir != prev_dir and new_dir != 180:
                break
        else:
            prev_dir = new_dir
    prev_dir = new_dir
    t_pos = t.pos()
    if (t_pos[0] > 300 or t_pos[0] < -300 or
            t_pos[1] > 300 or t_pos[1] < -300):
        t.pu()
        t.setpos(0, 0)
        t.pd()
    t.right(new_dir)
    t.forward(20)

screen.exitonclick()
