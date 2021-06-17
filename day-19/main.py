from turtle import Turtle, Screen

ti = Turtle()
screen = Screen()

def move_forwards():
    ti.forward(10)
def turn_right():
    new_h = ti.heading()-10
    ti.setheading(new_h)
def turn_left():
    new_h = ti.heading()+10
    ti.setheading(new_h)
def move_backwards():
    ti.backward(10)
def clear():
    ti.pu()
    ti.clear()
    ti.home()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()