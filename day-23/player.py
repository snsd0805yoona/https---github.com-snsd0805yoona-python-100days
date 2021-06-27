from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.seth(90)
        self.goto(STARTING_POSITION)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        return False

    def reset(self):
        self.goto(STARTING_POSITION)