from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)


screen.listen()

# vvv passing a function as an input to a function vvv
screen.onkey(key = "space", fun = move_forwards) # adding a () to the function forces the function to run immediately, we want it to wait for the keystroke

screen.exitonclick()