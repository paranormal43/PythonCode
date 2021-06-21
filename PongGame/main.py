from turtle import Screen,Turtle
from screen import MainScreen, PaddleLeft, PaddleRight
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game Ja")
screen.tracer(0)

#Cee Code
# m_screen = MainScreen()
# l_paddle = PaddleLeft()
# r_paddle = PaddleRight()

ball = Ball()
scoreboard = ScoreBoard()
center_line = MainScreen()

#Dr.Angela Code

l_paddle = Paddle(-380,0)  #can write : l_paddle = Paddle((-390,0)) and class should be __init__(self,position)
r_paddle = Paddle(370, 0)


# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()
# paddle.goto(380,0)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(),new_y)


screen.listen()

# #Cee Code
# screen.onkey(l_paddle.up, "w")
# screen.onkey(l_paddle.down, "s")
# screen.onkey(r_paddle.up, "Up")
# screen.onkey(r_paddle.down, "Down")

#Dr. Angela Code
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()


    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 340 or ball.distance(l_paddle) < 30 and ball.xcor() < -340:
        ball.bounce_x()


    # Detect R Paddle miss
    if ball.xcor() > 400:
        scoreboard.increase_score_l()
        ball.ball_reset()

    elif ball.xcor() < -400:
        scoreboard.increase_score_r()
        ball.ball_reset()








screen.exitonclick()

























screen.exitonclick()