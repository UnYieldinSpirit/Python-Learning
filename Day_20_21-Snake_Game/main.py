from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    screen.listen()

    # detects input from user to determine the movement of the snake
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")

    # detect collision with food
    if snake.head.distance(food) <= 10:
        snake.extend()
        food.new_location()
        scoreboard.increase_score()
        scoreboard.rewrite()
    
    # detect collision with wall
    if (snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # detect collision with other segments
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) <= 10:
            scoreboard.reset()
            snake.reset()
            
screen.exitonclick()