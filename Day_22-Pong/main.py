from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 1200, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
player_1 = Paddle((-300, 200))

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)

    screen.listen()

    screen.onkey(scoreboard.increase_left, "e")


    
screen.exitonclick()