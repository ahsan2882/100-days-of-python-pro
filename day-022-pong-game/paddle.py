from turtle import Turtle
import enum


class PaddlePostion(enum.Enum):
    LEFT = -350
    RIGHT = 350


class Paddle:
    def __init__(self, position):
        self.position = position
        self.paddle = []
        self.create_paddle()

    def create_paddle(self):
        for i in range(5):
            paddle_segment = Turtle(shape='square')
            paddle_segment.color('white')
            paddle_segment.penup()
            paddle_segment.goto(self.position.value, (i-2)*20)
            self.paddle.append(paddle_segment)

    def move_up(self):
        if self.paddle[4].ycor() < 250:
            for paddle_segment in self.paddle:
                paddle_segment.goto(
                    paddle_segment.xcor(),
                    paddle_segment.ycor()+20
                )

    def move_down(self):
        if self.paddle[0].ycor() > -250:
            for paddle_segment in self.paddle:
                paddle_segment.goto(
                    paddle_segment.xcor(),
                    paddle_segment.ycor()-20
                )
