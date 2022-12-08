from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_move = 0.2
        self.y_move = 0.2
        # self.setheading(45)

    def move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto(newX, newY)

    def bounce(self):
        self.y_move *= -1
