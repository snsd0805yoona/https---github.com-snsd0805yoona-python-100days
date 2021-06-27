import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    #detect collision
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #detect player reach the finish line

    if player.is_at_finish_line():
        player.reset()
        score.level_up()
        car.speed_up()

screen.exitonclick()
