from turtle import Turtle


class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-390, 290)
        self.pendown()
        self.goto(390, 290)
        self.right(90)
        self.goto(390, -290)
        self.right(90)
        self.goto(-390, -290)
        self.right(90)
        self.goto(-390, 290)
