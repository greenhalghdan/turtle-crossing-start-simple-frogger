STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.set_starting_position()
        self.setheading(90)
        self.shape("turtle")

    def north(self):
        self.setheading(90)
        self.forward(10)

    def set_starting_position(self):
        self.goto(0, -280)