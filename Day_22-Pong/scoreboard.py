from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.pensize()
        self.goto(-400 , 200)
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.write(f"{self.left_score}", font = ('ArcadeClassic', 90, "normal"), align = "center")
        self.goto(400, 200)
        self.write(f"{self.right_score}", font = ('ArcadeClassic', 90, "normal"), align = "center")
    
    def increase_score(self, side):
        '''Update the score displayed depending on which side the ball ends the round (opposite-ish)'''
        if side == "right":
            self.left_score += 1
        elif side == "left":
            self.right_score += 1
        self.rewrite()

    def rewrite(self):
        '''Updates the score displayed on the screen'''
        self.clear()
        self.goto(-400 , 200)
        self.write(f"{self.left_score}", font = ('ArcadeClassic', 90, "normal"), align = "center")
        self.goto(400, 200)
        self.write(f"{self.right_score}", font = ('ArcadeClassic', 90, "normal"), align = "center")

    def game_over(self):
        self.clear()
        self.goto(0)
        self.write("Game Over")

    