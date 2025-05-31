from turtle import Turtle
from turtle import Screen
from turtle import Shape

shape = Shape

RECTCOORS = ((-20,10),(20,10),(20,-10),(-20,-10))

class Paddle:

    def __init__(self, position):
        self.position = position
        self.paddle = self.create_paddle()

    def create_paddle(self):
        turtle = Turtle
        turtle.penup()
        turtle.color("white")
        turtle.goto(self.position)
        turtle.shape("square")
        turtle.shapesize(stretch_len = 5, stretch_wid = 2)
        return turtle
