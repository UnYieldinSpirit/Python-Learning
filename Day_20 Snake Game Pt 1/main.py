from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snaked Up")
screen.tracer(0)

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
screen.update()

game_is_on = True

while game_is_on == True:
    screen.update()
    time.sleep(0.5)

    for segment in range(len(snake_body) - 1, 0, -1):
        x_coor = snake_body[segment - 1].xcor()
        y_coor = snake_body[segment - 1].ycor()
        snake_body[segment].goto(x_coor, y_coor)
    snake_body[0].forward(20)

# Have the current segment save it position and then have the previous segment assume that location.

screen.exitonclick()