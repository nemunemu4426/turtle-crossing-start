import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    car_manager.generate_car()

    if player.ycor() > 280:
        player.refresh()
        scoreboard.increase_level()
        car_manager.increase_speed()
    
    if car_manager.detect_collision_with_player(player):
        scoreboard.game_over()
        game_is_on = False
    
screen.exitonclick()
