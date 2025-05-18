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
    time.sleep(0.09)

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
    if ((snake.head.xcor() == -300 or snake.head.xcor() == 300) or (snake.head.ycor() == -300 or snake.head.ycor() == 300)):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with other segments
    for segment in range(len(snake.snake_body) -1, 1, -1):
        if snake.head.distance(snake.snake_body[segment]) <= 10:
            game_is_on  = False
            scoreboard.game_over() 

screen.exitonclick()