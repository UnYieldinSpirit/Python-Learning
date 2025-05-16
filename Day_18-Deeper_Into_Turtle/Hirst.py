import colorgram
from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
timmy = Turtle()
timmy.width(25)
timmy.speed("fastest")
timmy.hideturtle()

number_of_dots = 100

# Commented out colorgram extractions...
# colors = colorgram.extract('image.jpg', 30)

# color_list = []

# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b

#     new_color = (r, g, b)
#     color_list.append(new_color)

painting_colors = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

def setup():
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)

def dot_maker():
    for _ in range(10):
        timmy.dot(20, random.choice(painting_colors))
        timmy.forward(50)

def reset_left():
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.forward(50)

def reset_right():
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)

def hirst():
    setup()
    for _ in range(5):
        dot_maker()
        reset_right()
        dot_maker()
        reset_left()

def hirst_simple():
    setup()
    for dot_count in range(1, number_of_dots + 1):
        timmy.dot(20, random.choice(painting_colors))
        timmy.forward(50)

        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

hirst_simple()

screen = Screen()
screen.exitonclick()