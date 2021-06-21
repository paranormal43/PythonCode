from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.score_a()
        self.score_b()


    def score_a(self):
        self.goto(-250, 250)
        self.write(f"Score : {self.score_l}", font=("Arial", 20, "normal"))

    def score_b(self):
        self.goto(150, 250)
        self.write(f"Score : {self.score_r}", font=("Arial", 20, "normal"))

    def update_scoreboard(self):
        self.goto(-250, 250)
        self.write(f"Score : {self.score_l}", font=("Arial", 20, "normal"))
        self.goto(150, 250)
        self.write(f"Score : {self.score_r}", font=("Arial", 20, "normal"))

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()
