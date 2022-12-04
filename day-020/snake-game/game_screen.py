from turtle import Screen
import time


class GameScreen():
    def __init__(self, up, down, left, right):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.listen()
        self.screen.onkeypress(up, "Up")
        self.screen.onkeypress(down, "Down")
        self.screen.onkeypress(left, "Left")
        self.screen.onkeypress(right, "Right")

    def update(self):
        time.sleep(0.8)
        self.screen.update()

    def exitGame(self):
        self.screen.exitonclick()
