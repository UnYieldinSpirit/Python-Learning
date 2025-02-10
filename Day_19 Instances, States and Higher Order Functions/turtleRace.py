from turtle import Turtle, Screen
import random as random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make Your Bet", prompt = "Which turtle will win the race? Enter a color: ")

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

y_position = -100

finish = False

def setup(turtle, y_position, color):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x = -250, y = y_position)
    turtle_list.append(turtle)

def race(list):
    global finish
    while finish == False:
        list[random.randint(0, len(list) - 1)].forward(random.randint(a = 1, b = 5))
        for i in turtle_list:
            finish = check(i)
            if finish == True:
                break
    check_winnings(user_bet, winner)

def check(turtle):
    '''Checks to see if a turtle has crossed the finish line'''
    global winner
    if turtle.xcor() >= 225:
        winner = turtle
        return True
    else:
        return False

def check_winnings(bet, winning_turtle): #FIX THIS, THIS IS THE FINAL PORTION
    if bet == winning_turtle.fillcolor():
        print("RIGHT!")
    else:
        print("COULD YOU BE ANYMORE WRONG...")

for i in color_list:
    setup(turtle = i, y_position = y_position, color = i)
    y_position += 40

race(turtle_list)

# mayo
# sriracha

screen.exitonclick()

# TODO - Make 6 turtles line up on the left side of the screen
# TODO - Each turtle should be a different color - red, orange, yellow, green, blue, purple 
# TODO - Race forward at random increments
# TODO - Store the winner
# TODO - Compare winner to guess 