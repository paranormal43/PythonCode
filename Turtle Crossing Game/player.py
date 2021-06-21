from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        self.position_reset()
        self.setheading(90)

    def up(self):
        position = self.ycor()
        self.goto(self.xcor(),position+MOVE_DISTANCE)

    def down(self):
        position = self.ycor()
        self.goto(self.xcor(),position-MOVE_DISTANCE)

    def left(self):
        position = self.xcor()
        self.goto(position - MOVE_DISTANCE,self.ycor())

    def right(self):
        position = self.xcor()
        self.goto(position + MOVE_DISTANCE, self.ycor())

    def position_reset(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False