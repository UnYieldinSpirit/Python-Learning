from turtle import Turtle

UP = 90
DOWN = 270
MOVE_SPEED = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.color("white")
        self.goto(self.position)
        self.shape("square")
        self.shapesize(stretch_len = 5, stretch_wid = 1)
        self.setheading(UP)

    def up(self):
        '''Handles the movement of the paddle upwards'''
        self.setheading(UP)
        self.forward(MOVE_SPEED)

    def down(self):
        '''Handles the movement of the paddle upwards'''
        self.setheading(DOWN)
        self.forward(MOVE_SPEED)
