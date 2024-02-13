from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.move()

    def move(self):
        xgoto = random.randint(-260, 260)
        ygoto = random.randint(-260, 260)
        self.goto(xgoto, ygoto)
