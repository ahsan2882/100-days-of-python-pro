from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        # self.x_move = 0.2
        # self.y_move = 0.2
        self.setheading(45)

    def move(self):
        self.forward(0.4)

    def bounce(self, heading):
        self.setheading(heading)

    def reset(self):
        self.home()
        self.setheading(choice([45, 135, 225, 315]))
