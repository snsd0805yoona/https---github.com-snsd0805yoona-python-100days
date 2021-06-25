from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

p1 = Player((350, 0))
p2 = Player((-350, 0))
ball = Ball()
score =Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=p1.up)
screen.onkey(key="Down", fun=p1.down)
screen.onkey(key="w", fun=p2.up)
screen.onkey(key="s", fun=p2.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    #detect collision of the paddle
    if ball.distance(p1)<50 and ball.xcor() > 320 or ball.distance(p2)<50 and ball.xcor() <-320:
        ball.hit()

    #detect if paddle miss the ball
    if ball.xcor() >380 or ball.xcor() <-380:
        if ball.xcor()>0:
            score.add("p2")
        elif ball.xcor()<0:
            score.add("p1")
        
        ball.reset_position()

screen.exitonclick()