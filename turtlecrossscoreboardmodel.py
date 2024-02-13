from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0
        self.goto(-480, 280)
        self.update()


    def addpoint(self):
        self.score += 1
        self.update()


    def update(self):
        self.clear()
        self.write("Score: " + str(self.score))


    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center")
        self.showturtle()
