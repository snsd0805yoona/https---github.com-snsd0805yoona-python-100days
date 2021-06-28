from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self) -> None:
        self.snake=[]
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)
    
    def add_segment(self, position):
        segment_1 = Turtle(shape="square")
        segment_1.speed("fastest")
        segment_1.color("white")
        segment_1.pu()
        segment_1.goto(position)
        self.snake.append(segment_1)

    def move(self):
        for seg_num in range(len(self.snake)-1 , 0 ,-1 ):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.seth(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.seth(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:    
            self.head.seth(LEFT)
    
    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def reset(self):
        for i in self.snake:
            i.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]



