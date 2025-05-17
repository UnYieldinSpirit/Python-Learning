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
        self.goto(-150, -260)
        
    def new_location(self):
        x_coor = random.choice(range(-280, 280, 20))
        y_coor = random.choice(range(-280, 280, 20))

        self.goto(x_coor, y_coor)

    def return_position(self):
        print(self.position())
        return self.position()
