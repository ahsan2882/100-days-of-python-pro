from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard(0, 0)

    def update_scoreboard(self, player1_score, player2_score):
        self.clear()
        self.goto(0, 240)
        self.write("Scoreboard\n", align=ALIGNMENT, font=FONT)
        self.goto(0, 220)
        self.write(f"Player 1: {player1_score}\n", align=ALIGNMENT,
                   font=FONT)
        self.goto(0, 200)
        self.write(f"Player 2: {player2_score}\n", align=ALIGNMENT,
                   font=FONT)
