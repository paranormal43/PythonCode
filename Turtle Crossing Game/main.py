from turtle import Screen
from player import Player
import time
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")


player = Player()
car = CarManager()
scoreboard = ScoreBoard()

screen.onkey(player.up, "Up")
# screen.onkey(player.down, "Down")
# screen.onkey(player.left, "Left")
# screen.onkey(player.right, "Right")


game_is_on = True
while game_is_on:
    count = 0
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if player.is_at_finish_line():
        player.position_reset()
        scoreboard.increase_score()
        car.level_up()

    for car_inside in car.car_list:
        if player.distance(car_inside) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
