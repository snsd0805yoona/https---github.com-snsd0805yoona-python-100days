from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__() 
        self.pu()
        self.hideturtle()
        self.color("white")
        self.score=0
        self.goto(0, 270)
        self.write("Score: "+str(self.score), False, align="center", font=("Arial", 18, "normal"))
    
    def add_Score(self):
        self.clear()
        self.score+=1
        self.write("Score: "+str(self.score), False, align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 18, "normal"))