from turtle import Turtle

MOVE_SPEED = 10
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.home()
        self.x_move = MOVE_SPEED
        self.y_move = MOVE_SPEED
        self.move_speed = 0.1
    
    def reset(self):
        self.home()
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move        
        self.goto(new_xcor, new_ycor)

    def wall_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
