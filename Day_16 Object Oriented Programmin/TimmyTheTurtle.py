# import turtle
# can import it like that or you can import it like this:
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink")

my_screen = Screen()
print(my_screen.canvheight) # accessing the attribute that is tied to the Screen() object
my_screen.exitonclick()