from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.mode("logo")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

screen.update()

is_game_on = True
while is_game_on:
    if player.reach_end():
        # increase score level and car speed
        player.reset()
        scoreboard.increase_level()
        carManager.increase_speed()
    for car in carManager.cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()
    carManager.move_cars()
    if scoreboard.level % 5 == 0:
        carManager.increase_cars()
    carManager.manage_cars()
    screen.update()

screen.exitonclick()
