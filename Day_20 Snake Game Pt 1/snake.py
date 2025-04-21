from turtle import Turtle
import time

class Snake:

    def __init__(self):
        self.snake_body = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_body()

    def create_body(self):
        for position in self.starting_positions:
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(position)
            self.snake_body.append(turtle)

    def move(self):
        for segment in range(len(self.snake_body) -1, 0, -1):
            x_coor = self.snake_body[segment - 1].xcor()
            y_coor = self.snake_bodys[segment - 1].ycor()
            self.snake_body[segment].goto(x_coor, y_coor)
        self.snake_body[0].forward(20)