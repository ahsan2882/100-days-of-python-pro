from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.spawning_limitX = screen.window_width()/2 - 20
        self.spawning_limitY = screen.window_height()/2 - 20
        randomX = randint(-self.spawning_limitX, self.spawning_limitX)
        randomY = randint(-self.spawning_limitY, self.spawning_limitY)
        self.goto(randomX, randomY)

    def refresh(self):
        self.hideturtle()
        randomX = randint(-self.spawning_limitX, self.spawning_limitX)
        randomY = randint(-self.spawning_limitY, self.spawning_limitY)
        self.goto(randomX, randomY)
        self.showturtle()
