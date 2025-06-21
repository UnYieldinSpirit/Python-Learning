from turtle import Turtle

# prolly best to make these a constant as they will NEVER change and are integral to the functioning of the game
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
        '''Initial creation of the snake's body'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        '''Adding a segment to the end of the snake body'''
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.snake_body.append(turtle)

    def extend(self):
        '''Increases the snake body by one segment on the tail end of the snake'''
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        '''Manages the movement of the snake, moving the head first and having each segment of the body follow suit'''
        for segment in range(len(self.snake_body) -1, 0, -1):
            x_coor = self.snake_body[segment - 1].xcor()
            y_coor = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(x_coor, y_coor)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        '''Changes the movement direction of the snake right'''
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def up(self):
        '''Changes the movement direction of the snake up'''
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def left(self):
        '''Changes the movement direction of the snake left'''
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def down(self):
        '''Changes the movement direction of the snake down'''
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)