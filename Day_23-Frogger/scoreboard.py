FONT = ("Courier", 24, "normal")
FONT_2 = ("Courier", 32, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("black")
        self.penup()
        self.pensize()
        self.goto(-400 , 200)
        self.hideturtle()
        self.level = 0
        self.rewrite()
    
    def increase_level(self):
        '''Increase the level that the player is on'''
        self.level += 1        
        self.rewrite()

    def rewrite(self):
        '''Updates the level displayed on the screen'''
        self.clear()
        self.goto(-300 , 250)
        self.write(f"Level: {self.level}", font = FONT)

    def game_over(self):
        '''Handles the printing of the Game Over screen'''
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", font = FONT_2, align = "center")
        self.goto(0, -100)
        self.write(f"Level: {self.level}", font = FONT_2, align = "center")