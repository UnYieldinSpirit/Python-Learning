from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snaked Up")

# set three turtles to squares in a row, 1st at (0,0)

snake_body = []

def setup():
    x_coordinate = 0
    for i in range(0, 3):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.turtlesize()
        turtle.setx(x_coordinate)
        x_coordinate -= 20
        snake_body.append(turtle)

setup()
screen.exitonclick()