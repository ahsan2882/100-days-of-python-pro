from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear():
    t.clear()
    t.pu()
    t.home()
    t.pd()


t.shape('turtle')
s.listen()

s.onkey(move_backwards, 's')
s.onkey(move_forwards, 'w')
s.onkey(turn_left, 'a')
s.onkey(turn_right, 'd')
s.onkey(clear, 'c')

s.exitonclick()
