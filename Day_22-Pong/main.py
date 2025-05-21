from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 1200, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)

    game_is_on = False
    
screen.exitonclick()