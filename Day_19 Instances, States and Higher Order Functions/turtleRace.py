from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
# user_bet = screen.textinput(title = "Make Your Bet", prompt = "Which turtle will win the race? Enter a color: ")

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []


def setup(turtle, y_position, color):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x = -250, y = y_position)
    turtle_list.append(turtle)

def check_winnings(bet, winning_turtle):
    if user_bet == winning_turtle.color:
        print("You win!")
    else:
        print("You Lose")

j = -100
lift = 0

for i in color_list:
    setup(turtle = i, y_position = j, color = i)
    j += 40

screen.exitonclick()

# TODO - Make 6 turtles line up on the left side of the screen
# TODO - Each turtle should be a different color - red, orange, yellow, green, blue, purple 
# TODO - Race forward at random increments
# TODO - Store the winner
# TODO - Compare winner to guess 