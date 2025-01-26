from turtle import Turtle, Screen
import pandas as panda #aliasing a module allows you the ability to call the module with your own naming convention
import random as rand
import heroes
# in order to use a module, you have to install it first. These allow you to pull in certain modules when you need it, so the file isn't huge with a bunch of modules

colors = ["red", "blue", "orange", "pink", "green", "purple", "yellow"]
turns = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

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

def clockwise_circle(size):
    for i in range(360):
        timmy.forward(size)
        timmy.right(1)

def counter_circle(size):
    for i in range(360):
        timmy.forward(size)
        timmy.left(1)

def eight(size):
     clockwise_circle(size)
     counter_circle(size)

def forward_dashed_line(length):
     for i in range(length):
          timmy.forward(10)
          timmy.penup() # stops turtle from drawing
          timmy.forward(10)
          timmy.pendown() # restarts turtle's drawing

def print_shapes(size):
    triangle(size)
    square(size)
    pentagon(size)
    hexagon(size)
    heptagon(size)
    octagon(size)
    nonagon(size)
    decagon(size)

def draw_shape(num_of_sides, size):
    angle = 360 / num_of_sides
    for i in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)

def rand_walk(size):
    timmy.pensize(10)
    timmy.speed("fastest")
    for i in range(rand.randint(0, 100)):
        timmy.color(rand.choice(colors))
        timmy.forward(size)
        timmy.right(rand.choice(turns))

rand_walk(30)

print(heroes.gen())

# for shape_side in range(3, 11):
#     draw_shape(shape_side, 100)

# TODO - Create and manage tuples

screen = Screen()
screen.exitonclick()