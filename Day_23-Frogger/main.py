import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

score = Scoreboard()
manager = CarManager()

player = Player()

game_is_on = True
loop = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()

    if (loop % 5) == 0:
        manager.gen_car()

    for car in manager.cars_on_screen:
        if car.xcor() >= -300:
            del car
    
    manager.forward()

    screen.onkey(player.move, "space")

    # reset the player for the next level
    if player.ycor() >= 280:
        player.reset()
        score.increase_level()
        manager.increase_speed()

    # collision detection
    for car in manager.cars_on_screen:
        if car.distance(player) <= 15:
            game_is_on = False
            score.game_over()

    loop += 1