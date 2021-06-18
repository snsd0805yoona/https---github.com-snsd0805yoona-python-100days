from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Enter the color of turtle who will win the race: ")

colors =["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(0, 6):
    ti = Turtle(shape="turtle")
    ti.penup()
    ti.color(colors[i])
    ti.goto(x=-230, y=80-i*30)
    turtles.append(ti)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You win the game! The {win_color} win!")
            else:
                print(f"You lose the game! The {win_color} win!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()