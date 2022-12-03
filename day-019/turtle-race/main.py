from turtle import Turtle, Screen
from random import randint

s = Screen()
s.setup(width=500, height=400)

user_bet = s.textinput(title="Make your bet",
                       prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def move_forward(turt):
    turt.forward(randint(0, 10))


turtles = []
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.pu()
    t.goto(x=-230, y=-100 + colors.index(color) * 40)
    turtles.append(t)

is_race_finished = False
while not is_race_finished:
    for turt in turtles:
        if turt.xcor() > 230:
            winner = turt.pencolor()
            is_race_finished = True
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            break
        move_forward(turt)
s.exitonclick()
