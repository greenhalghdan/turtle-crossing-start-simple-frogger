FONT = ("Courier", 24, "normal")

'''Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful 
crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. 
If you get stuck, check the video walkthrough in Step 7.'''

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 250)
        self.current_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def current_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def increase_level(self):
        self.level += 1
