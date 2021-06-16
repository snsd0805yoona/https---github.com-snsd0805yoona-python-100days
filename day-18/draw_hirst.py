import turtle as t
import colorgram
import random

ti = t.Turtle()
t.colormode(255)
rgb_colors = []
colors = colorgram.extract("hirst.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

def draw_dot(size, n, length, color):
    for i in range(n):
        curr_y=ti.ycor()
        curr_x=ti.xcor()
        for x in range(n):
            ti.pd()
            ti.dot(size, random.choice(color))
            ti.pu()
            ti.forward(length)
        ti.goto(curr_x, curr_y+length) 

ti.hideturtle()   
ti.speed("fastest")
ti.pu()  
ti.setheading(225)
ti.forward(300)
ti.setheading(0)
draw_dot(20, 10, 50, rgb_colors)
Screen=t.Screen()
Screen.exitonclick()