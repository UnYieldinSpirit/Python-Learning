from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
screen = Screen()
screen.setup(width = 1200, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
player_1 = Paddle((-575, 200))
player_2 = Paddle((575, 200))

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.09)

    ball.move()
    screen.listen()

    # Reset paddles if out of the set parameters
    if player_1.ycor() <= -240:
        player_1.goto(-575, -240)

    if player_2.ycor() <= -240:
        player_2.goto(575, -240)
        
    if player_1.ycor() >= 240:
        player_1.goto(-575, 240)

    if player_2.ycor() >= 240:
        player_2.goto(575, 240) 
    
    # player 1 controls
    screen.onkey(player_1.down, "s")
    screen.onkey(player_1.up, "w")

    # player 2 controls
    screen.onkey(player_2.up, "Up")
    screen.onkey(player_2.down, "Down")

    # ceiling detection and bounce
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.wall_bounce()
    
    if (ball.distance(player_1) <= 20) or (ball.distance(player_2) <= 20):
        ball.paddle_bounce() 

    print(ball.xcor())
    if ball.xcor() <= -600:
        scoreboard.increase_score("right")
        ball.reset()
    if ball.xcor() >= 600:
        scoreboard.increase_score("left")
        ball.reset()
        
screen.exitonclick()