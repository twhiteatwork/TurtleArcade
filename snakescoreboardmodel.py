from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.highscore = 0
        self.readhighscore()
        self.update()


    def addpoint(self):
        self.score += 1


    def update(self):
        self.clear()
        self.goto(-270,280)
        self.write("Score: " + str(self.score), align="center")
        self.goto(280, 280)
        self.write("High score: " + str(self.highscore), align="right")


    def writehighscore(self):
        self.highscore = self.score
        with open("./snakehighscore.txt", mode="w") as file:
            file.write(str(self.highscore))


    def readhighscore(self):
        with open("./snakehighscore.txt") as file:
            self.highscore = int(file.read())


    def gameover(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update()
            self.writehighscore()
        self.goto(0,0)
        self.write("GAME OVER", align="center")
