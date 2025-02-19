from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snaked Up")

# set three turtles to squares in a row, 1st at (0,0)

snake_body = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    turtle = Turtle("square")
    turtle.color("white")
    turtle.goto(position)
    snake_body.append(turtle)

screen.exitonclick()