from turtle import Turtle

class Scoreboard(Turtle):
    
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
        '''Increases the user's score by one whenever the user collects a food pellet'''
        self.score += 1

    def rewrite(self):
        '''Updates the score displayed on the screen'''
        self.clear()
        self.write(f"Score: {self.score}", font = ('Arial', 40, "normal"))

    def game_over(self):
        '''Ends the game'''
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER - FINAL SCORE: {self.score}", font = ('Comic Sans', 30, 'normal'), align = 'center')