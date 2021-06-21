from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-290, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Level : {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over Na Ja 555", align="center",font=FONT)
