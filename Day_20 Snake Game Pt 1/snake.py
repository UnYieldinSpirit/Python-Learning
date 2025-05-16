from turtle import Turtle

#prolly best to make these a constant as they will NEVER change and are integral to the functioning of the game
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

    def create_body(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(position)
            self.snake_body.append(turtle)

    def move(self):
        for segment in range(len(self.snake_body) -1, 0, -1):
            x_coor = self.snake_body[segment - 1].xcor()
            y_coor = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(x_coor, y_coor)
        self.head.forward(MOVE_DISTANCE)
        if(self.head.xcor() < -300):
            self.reset_right()
        if(self.head.xcor() > 300):
            self.reset_left()
        if(self.head.ycor() < -300):
            self.reset_top()
        if(self.head.ycor() > 300):
            self.reset_bottom()
        # print(self.head.position())
    
    def reset_right(self):
        y_coor = self.head.ycor()
        x_coor = 300
        self.head.goto(x_coor, y_coor)

    def reset_left(self):
        y_coor = self.head.ycor()
        x_coor = -300
        self.head.goto(x_coor, y_coor)        

    def reset_top(self):
        y_coor = 300
        x_coor = self.head.xcor()
        self.head.goto(x_coor, y_coor)

    def reset_bottom(self):
        y_coor = -300
        x_coor = self.head.xcor()
        self.head.goto(x_coor, y_coor)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)        

