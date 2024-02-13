import random
from turtle import Turtle


COLORS = ["red", "green", "blue", "yellow", "purple"]
MOVESPEEDS = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
DIFFICULTY_NORMAL = 40
MOVESPEED_DEFAULT = 40


class Car(Turtle):


    def __init__(self, lane):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.difficulty = DIFFICULTY_NORMAL
        self.movespeed = MOVESPEED_DEFAULT
        self.x = 520
        self.lane = lane #y
        self.create()

    
    def create(self):
        self.color(random.choice(COLORS))
        self.movespeed = random.choice(MOVESPEEDS) + MOVESPEED_DEFAULT - self.difficulty
        self.move()


    def reset(self):
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.movespeed = random.choice(MOVESPEEDS) + MOVESPEED_DEFAULT - self.difficulty
        self.x = 520
        self.move()


    def move(self):
        self.x = self.x - self.movespeed
        self.goto(self.x, self.lane)
        self.showturtle()
    