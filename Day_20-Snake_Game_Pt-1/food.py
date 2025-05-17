from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.pencolor("white")
        self.fillcolor("white")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.goto(random.choice(range(-280, 280, 20)), random.choice(range(-280, 280, 20)))
        
    def new_location(self):
        # random choice and range allows for the food pellet to change its location while remaining on the screen
        x_coor = random.choice(range(-280, 280, 20))
        y_coor = random.choice(range(-280, 280, 20))

        self.goto(x_coor, y_coor)