from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    # Create a new car every time, then random choice = 1
    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("turtle")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(2, 2)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(310, new_y)
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
