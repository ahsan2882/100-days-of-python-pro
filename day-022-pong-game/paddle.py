from turtle import Turtle
import enum


class PaddlePostion(enum.Enum):
    LEFT = -350
    RIGHT = 350


class Paddle:
    def __init__(self, position):
        self.paddle = self.createPaddle(position)

    def createPaddle(self, position):
        paddle = []
        for i in range(5):
            paddle_segment = Turtle(shape='square')
            paddle_segment.color('white')
            paddle_segment.penup()
            paddle_segment.goto(position.value, (2-i)*20)
            paddle.append(paddle_segment)

        return paddle

    def move_up(self):
        head = self.paddle[0]
        if head.pos()[1] < 280:
            for paddle_segment in range(len(self.paddle)-1, 0, -1):
                self.paddle[paddle_segment].goto(
                    self.paddle[paddle_segment-1].pos())
            head.forward(20)

    def move_down(self):
        head = self.paddle[-1]
        if head.pos()[1] > -280:
            for paddle_segment in range(0, len(self.paddle)-1, 1):
                self.paddle[paddle_segment].goto(
                    self.paddle[paddle_segment+1].pos()
                )
            head.back(20)
