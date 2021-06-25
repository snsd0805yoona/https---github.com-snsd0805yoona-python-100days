from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.speed("fastest")
        self.move_speed=0.1
    
    def move(self):
        new_xcor = self.xcor()+self.xmove
        new_ycor = self.ycor()+self.ymove
        self.goto(new_xcor, new_ycor)

    def bounce(self):
        self.ymove *=-1
        
    
    def hit(self):
        self.xmove *=-1
        self.move_speed*=0.5
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.hit()