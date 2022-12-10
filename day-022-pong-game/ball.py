from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.speed = 0.2
        # self.x_move = 0.2
        # self.y_move = 0.2
        self.setheading(45)

    def move(self):
        self.forward(self.speed)

    def bounce(self, heading):
        self.setheading(heading)

    def reset(self):
        self.home()
        self.speed = 0.2
        self.setheading(choice([45, 135, 225, 315]))

    def increase_speed(self):
        self.speed += 0.1
