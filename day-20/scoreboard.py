from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__() 
        self.pu()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        
        self.hideturtle()
        self.color("white")
        self.score=0
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Arial", 18, "normal"))
    
    def add_Score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Arial", 18, "normal"))

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Arial", 18, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        
        self.score=0
        self.update()

    
        