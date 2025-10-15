from turtle import Turtle
FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.pensize()
        self.goto(0, 260)
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.rewrite()

    def increase_score(self):
        '''Increases the user's score by one whenever the user collects a food pellet'''
        self.score += 1

    def rewrite(self):
        '''Updates the score displayed on the screen'''
        self.clear()
        self.write(f"Score: {self.score} Hi-Score: {self.high_score}", font = FONT, align = ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.rewrite()