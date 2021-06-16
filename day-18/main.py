import turtle as t
import random


ti = t.Turtle()
t.colormode(255)
# draw a square
# """ for i in range(1, 5):
#     t.forward(100)
#     t.right(90) """

# draw a dash line
# for i in range(101):
#     if i%2==0:
#         t.penup()
#     else:
#         t.pendown()
#     t.forward(10)

"""
    draw different angle shape
"""
# for i in range(3, 13):
#     for j in range(i):
#         t.forward(100)
#         t.right(360/i)

"""
    draw random path with rgb random color
"""
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# directions=[0, 90, 180, 270]
# ti.pensize(15)
ti.speed("fastest")

# for i in range(200):
#     ti.color(random_color())
#     ti.forward(30)
#     ti.setheading(random.choice(directions))

"""
    draw a spirograph
"""
def draw_spiro(size):
    for i in range(int(360/size)):
        ti.color(random_color())
        ti.circle(100)
        ti.setheading(ti.heading()+size)

draw_spiro(5)

Screen=t.Screen()
Screen.exitonclick()