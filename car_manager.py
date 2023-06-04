COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

'''Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left 
    edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe 
    zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, 
    check the video walkthrough in Step 4.'''

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE


    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)

    def add_new_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=4, stretch_wid=2)
        ycor = (random.randint(-260, 240))
        # self.xcor = 0
        new_car.goto(300, ycor)
        new_car.setheading(180)
        self.cars.append(new_car)

    '''Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left 
    edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe 
    zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, 
    check the video walkthrough in Step 4.'''