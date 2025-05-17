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
        """Updates the score displayed on the screen"""
        self.clear()
        self.write(f"Score: {self.score}", font = ('Arial', 40, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER - FINAL SCORE: {self.score}", font = ('Comic Sans', 30, 'normal'), align = 'center')