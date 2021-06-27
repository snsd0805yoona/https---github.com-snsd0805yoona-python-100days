from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color("Black")
        self.goto(-290, 260)
        self.level=1
        self.write(f"Level:{self.level}", False, "left", font = FONT)

    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level:{self.level}", False, "left", font = FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", False, "center", font = FONT)
        