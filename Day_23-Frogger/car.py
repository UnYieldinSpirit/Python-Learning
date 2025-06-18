from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, position, color):
        super().__init__() 
        self.position = position
        self.penup()
        self.color(color)
        self.goto(self.position)
        self.shape("square")
        self.shapesize(stretch_len = 2, stretch_wid = 0.6)
        self.setheading(180)

    def drive(self, speed):
        self.forward(speed)
