import colorgram as gram
from turtle import Turtle, Screen
import turtle as turtle
import pandas as panda #aliasing a module allows you the ability to call the module with your own naming convention
import random as rand
import heroes
# in order to use a module, you have to install it first. These allow you to pull in certain modules when you need it, so the file isn't huge with a bunch of modules

colors = ["red", "blue", "orange", "pink", "green", "purple", "yellow"]
turns = [0, 90, 180, 270]

turtle.colormode(255)
timmy = Turtle()
timmy.pensize(3)
timmy.shape("turtle")
timmy.speed(0)

def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def mutable_random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    rand_color = [r, g, b]
    return rand_color

def triangle(size):
    '''Draws a three-sided shape'''
    for i in range(3):
        timmy.forward(size)
        timmy.right(120)

def square(size):
    '''Draws a 4-sided shape'''
    for i in range(4):
        timmy.forward(size)
        timmy.right(90)

def pentagon(size):
    '''Draws a 5-sided shape'''
    for i in range(5):
        timmy.forward(size)
        timmy.right(72)

def hexagon(size):
    '''Draws a 6-sided shape'''
    for i in range(6):
        timmy.forward(size)
        timmy.right(60)

def heptagon(size):
    '''Draws a 7-sided shape'''
    for i in range(7):
         timmy.forward(size)
         timmy.right(51.43)

def octagon(size):
    '''Draws an eight-sided shape'''
    for i in range(8):
        timmy.forward(size)
        timmy.right(45)

def nonagon(size):
    '''Creates a nine-sided shape'''
    for i in range(9):
        timmy.forward(size)
        timmy.right(40)

def decagon(size):
     '''Draws a ten-sided shape'''
     for i in range(10):
        timmy.forward(size)
        timmy.right(36)

def eight(size):
     '''Draws a figure eight'''
     clockwise_circle(size)
     counter_circle(size)

def forward_dashed_line(length):
    '''Draws a dashed line forward at a pre-determined distance'''
    for i in range(length):
          timmy.forward(10)
          timmy.penup() # stops turtle from drawing
          timmy.forward(10)
          timmy.pendown() # restarts turtle's drawing

def print_shapes(size):
    '''Not so efficient means of drawing all sided shapes from triangle to decagon'''
    triangle(size)
    square(size)
    pentagon(size)
    hexagon(size)
    heptagon(size)
    octagon(size)
    nonagon(size)
    decagon(size)

def draw_shape(num_of_sides, size):
    '''Draws a shape based on the number of sides'''
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        timmy.forward(size)
        timmy.right(angle)

def rand_walk(length):
    '''Draws a randomized path of connected lines, all the same predetermined length'''
    timmy.pensize(10)
    timmy.speed("fastest")
    for i in range(rand.randint(0, 100)):
        timmy.color(rand.choice(colors))
        timmy.forward(length)
        timmy.right(rand.choice(turns))

def draw_all_shapes(size):
    for shape_side in range(3, 11):
        draw_shape(shape_side, size)

def spirograph(size, variation):
    startPosition = timmy.position()
    startHeading = timmy.heading()
    timmy.circle(size)
    timmy.right(variation)
    while ((timmy.position() != startPosition) and (timmy.heading() != startHeading)):
        print(timmy.position())
        print(timmy.heading())
        timmy.color(mutable_random_color())
        timmy.circle(size)
        timmy.right(variation)

spirograph(200, 4)

screen = Screen()
screen.exitonclick()