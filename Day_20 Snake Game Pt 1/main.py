from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snaked Up")

# set three turtles to squares in a row, 1st at (0,0)

game = "test"
snake_body = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    turtle = Turtle("square")
    turtle.penup()
    turtle.color("white")
    turtle.goto(position)
    snake_body.append(turtle)

def move():
    for i in snake_body:
        i.forward(5)

def north():
    for i in snake_body:
        i.setheading("north")

def east():
    for i in snake_body:
        i.setheading("east")

def south():
    for i in snake_body:
        i.setheading("south")

def west():
    for i in snake_body:
        i.setheading("west")


screen.onkey(key = "Up", fun = north)
screen.onkey(key = "Left", fun = west)
screen.onkey(key = "Right", fun = east)
screen.onkey(key = "Down", fun = south)

screen.exitonclick()