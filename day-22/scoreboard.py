from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.p1 = 0
        self.p2 = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.write(f"{self.p2} v.s {self.p1}", False, align="center", font=("Arial", 18, "normal"))
    
    def add(self, user: str):
        self.clear()
        if user=="p1":
            self.p1+=1
        elif user =="p2":
            self.p2+=1
        self.write(f"{self.p2} v.s {self.p1}", False, align="center", font=("Arial", 18, "normal"))