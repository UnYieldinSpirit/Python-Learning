from turtle import Turtle

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
        self.x_move = 10
        self.y_move = 10
    
    def reset(self):
        self.ball.home(0, 0)

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move        
        self.goto(new_xcor, new_ycor)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1