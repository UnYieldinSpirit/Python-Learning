from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, position):
        super().__init__() 
        self.position = position
        self.penup()
        self.color("white")
        self.goto(self.position)
        self.shape("square")
        self.shapesize(stretch_wid = 1)
        self.setheading(180)

    def drive(self):
        self.forward(randint(0, 20))
