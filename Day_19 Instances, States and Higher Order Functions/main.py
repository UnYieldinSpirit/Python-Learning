from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def rotate_clockwise():
    timmy.right(5)

def rotate_counter_clockwise():
    timmy.left(5)

def clear():
    timmy.setposition(x = 0, y = 0)
    timmy.setheading(0)
    screen.clearscreen() # DOESN'T WORK

screen.listen()

# vvv passing a function as an input to a function vvv
screen.onkey(key = "w", fun = move_forwards) # adding a () to the function forces the function to run immediately, we want it to wait for the keystroke
screen.onkey(key = "a", fun = rotate_counter_clockwise)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = rotate_clockwise)
screen.onkey(key = "c", fun = clear)


screen.exitonclick()