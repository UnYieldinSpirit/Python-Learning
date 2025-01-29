import colorgram
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
timmy = Turtle()
timmy.width(25)

colors = colorgram.extract('image.jpg', 30)

color_list = []

for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b

    new_color = (r, g, b)
    color_list.append(new_color)

def hirst_paint():
    pass


print(color_list)

painting_colors = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

# screen = Screen()
# screen.exitonclick()