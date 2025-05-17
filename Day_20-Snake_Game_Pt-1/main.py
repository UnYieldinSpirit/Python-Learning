from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)

    snake.move()
    
    screen.listen()

    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")
    # screen.onkey(pause, "Space")

    # if snake.return_distance(food.return_position()) <= 10:
    #     snake.add_segment()
    #     food.new_location()

    if snake.head.distance(food) <= 10:
        snake.add_segment()
        food.new_location()
        scoreboard.increase_score()
        scoreboard.rewrite()
    
    if ((snake.head.xcor() == -300 or snake.head.xcor() == 300) or (snake.head.ycor() == -300 or snake.head.ycor() == 300)):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()