from turtle import Screen,Turtle


class MainScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.line_center()
        # self.paddle_l()

    def line_center(self):
        screen = Screen()
        self.color("white")
        self.penup()
        pos_y = 300
        self.hideturtle()
        self.goto(0,pos_y)
        for _ in range(15):
            self.pendown()
            pos_y -= 20
            self.goto(0, pos_y)
            self.penup()
            pos_y -= 20
            self.goto(0, pos_y)


class PaddleLeft(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_l()

    def paddle_l(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.showturtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.turtlesize(stretch_wid=5, stretch_len=1)
        x_pos = -390
        y_pos = 0
        self.goto(x_pos, y_pos)

    def up(self):
        self.position = self.ycor()
        self.position += 10
        self.goto(self.xcor(),self.position)

    def down(self):
        self.position = self.ycor()
        self.position -= 10
        self.goto(self.xcor(),self.position)


class PaddleRight(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_r()

    def paddle_r(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.showturtle()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.turtlesize(stretch_wid=5, stretch_len=1)
        x_pos = 380
        y_pos = 0
        self.goto(x_pos, y_pos)

    def up(self):
        self.position = self.ycor()
        self.position += 10
        self.goto(self.xcor(),self.position)

    def down(self):
        self.position = self.ycor()
        self.position -= 10
        self.goto(self.xcor(),self.position)




