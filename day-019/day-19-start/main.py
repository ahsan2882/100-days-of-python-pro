from turtle import Turtle, Screen

t = Turtle()
w = Screen()


def move_forwards():
    t.forward(100)


w.listen()
w.onkey(key='space', fun=move_forwards)
w.exitonclick()
