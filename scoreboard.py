import turtle
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-200, 250)
        self.score = 1
        self.count_score()

    def count_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.count_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



