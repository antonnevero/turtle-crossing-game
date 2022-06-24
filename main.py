from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.cars_move()

    # Check if the player touch any car
    for cars in car.all_cars:
        if cars.distance(player) < 25:
            is_game_on = False
            scoreboard.game_over()

    # Check if player is go on finish line
    if player.ycor() > 280:
        player.next_level()
        scoreboard.level_up()
        car.speed_up()


screen.exitonclick()
