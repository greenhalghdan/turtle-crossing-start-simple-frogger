import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
random_list = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.north, key="Up")
times_run = 0
game_is_on = True
while game_is_on:
    scoreboard.current_level()
    car.move_car()
    time.sleep(0.1)
    screen.update()
    if times_run % 6 == 0:
        car.add_new_car()
    times_run += 1
    for item in car.cars:
        if player.distance(item) < 40:
            game_is_on = False
            scoreboard.game_over()
            print("you have walked into a car")
    if player.ycor() == 290:
        player.set_starting_position()
        car.increase_speed()
        scoreboard.increase_level()



'''Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful 
crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. 
If you get stuck, check the video walkthrough in Step 7.'''

screen.exitonclick()
