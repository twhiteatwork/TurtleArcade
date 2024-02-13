from turtle import Turtle


DIRECTION_UP = 90
SHOULDER_BOTTOM = -280
SHOULDER_TOP = 280
LANE_WIDTH = 40


class PTurtle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(DIRECTION_UP)
        self.movetostart()


    def moveforward(self):
        if self.ycor() < SHOULDER_TOP:
            self.forward(LANE_WIDTH)
            self.lane += LANE_WIDTH


    def movetostart(self):
        self.hideturtle()
        self.x = 0 # center
        self.lane = SHOULDER_BOTTOM
        self.goto(self.x, self.lane)
        self.showturtle()


    def isacrossfinishline(self):
        if self.lane == SHOULDER_TOP:
            return True
        else:
            return False
    