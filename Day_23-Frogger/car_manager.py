from car import Car
from random import randint, choice
 
COLORS = ["red", "orange", "black", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_on_screen = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def gen_car(self):
        new_car = Car((300, randint(-260, 260)), choice(COLORS))
        self.cars_on_screen.append(new_car)

    def forward(self):
        for car in self.cars_on_screen:
            car.drive(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
 
    def __del__(self):
        pass

# TODO - Despawn after certain x coordinate - use 'del' function