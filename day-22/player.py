from turtle import Turtle

class Player(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(position)
        self.speed("fastest")

    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
    