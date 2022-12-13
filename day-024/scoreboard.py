from turtle import Turtle
from os.path import exists, abspath
import pathlib
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        loc = pathlib.Path(__file__).parent.resolve()
        self.txt_file_loc = pathlib.Path(loc, "high_score.txt").resolve()
        if not exists(self.txt_file_loc):
            file = open(self.txt_file_loc, "w")
            self.high_score = 0
            file.write("0")
        else:
            file = open(self.txt_file_loc, "r")
            self.high_score = int(file.read())
        file.close()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.txt_file_loc, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
