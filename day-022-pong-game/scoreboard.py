from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard(0, 0)

    def update_scoreboard(self, player1_score, player2_score):
        self.clear()
        self.goto(-100, 240)
        self.write(player1_score, align=ALIGNMENT,
                   font=FONT)
        self.goto(100, 240)
        self.write(player2_score, align=ALIGNMENT,
                   font=FONT)
