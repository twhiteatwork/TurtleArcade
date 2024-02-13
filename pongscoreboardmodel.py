from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self, paddleside):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.paddleside = paddleside
        if paddleside == "left":
            self.goto(-480,280)
            self.update()
        elif paddleside == "right":
            self.goto(450, 280)
            self.update()
        else: # none, stay in center
            pass


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
