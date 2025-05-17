from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.pensize()
        self.goto(-120, 200)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", font = ('Arial', 40, "normal"))

    def increase_score(self):
        self.score += 1

    def rewrite(self):
        self.clear()
        self.write(f"Score: {self.score}", font = ('Arial', 40, "normal"))
