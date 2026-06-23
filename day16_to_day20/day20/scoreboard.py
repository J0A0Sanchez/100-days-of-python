from turtle import Turtle
from time import sleep

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def resetgame(self):
        self.score = 0
        self.goto(0, 260)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)
