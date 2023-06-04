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

'''
problem 1:
Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north
. If you get stuck, check the video walkthrough in Step 3.

Problem 2:
Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of 
the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our 
little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video
 walkthrough in Step 4.

Problem3: 

Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video 
walkthrough in Step 5.

problem 4:
Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
When this happens, return the turtle to the starting position and increase the speed of the cars. 
Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. 
If you get stuck, check the video walkthrough in Step 6.

Problem5:
Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a 
successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.
 If you get stuck, check the video walkthrough in Step 7.

'''

screen.exitonclick()
