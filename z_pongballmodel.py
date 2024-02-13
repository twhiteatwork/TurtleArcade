from turtle import Turtle

X_UPPER_BOUND = 500
X_LOWER_BOUND = -500
Y_UPPER_BOUND = 280
Y_LOWER_BOUND = -280
SURFACE_TOP = "top"
SURFACE_BOTTOM = "bottom"
SURFACE_LEFT = "left"
SURFACE_RIGHT = "right"
DIRECTION_UP_RIGHT = "up_right"
DIRECTION_UP_LEFT = "up_left"
DIRECTION_DOWN_LEFT = "down_left"
DIRECTION_DOWN_RIGHT = "down_right"
HEADING_UP_RIGHT = 20
HEADING_UP_LEFT = 160
HEADING_DOWN_LEFT = 200
HEADING_DOWN_RIGHT = 340


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.direction = DIRECTION_UP_RIGHT
        self.setheading(HEADING_UP_RIGHT)
        self.color("white")
        self.speed("fastest")


    def move(self):
        self.forward(20)
        #print(self.xcor(), self.ycor())


    def hashitleftwall(self):
        if (self.xcor() < X_LOWER_BOUND and
            self.ycor() < Y_UPPER_BOUND - 10 and
            self.ycor() > Y_LOWER_BOUND + 10):
            return True
        else:
            return False

    
    def hashitrightwall(self):
        if (self.xcor() > X_UPPER_BOUND and
            self.ycor() < Y_UPPER_BOUND - 10 and
            self.ycor() > Y_LOWER_BOUND + 10):
            return True
        else:
            return False


    def hashittopwall(self):
        if (self.ycor() > Y_UPPER_BOUND and
            self.xcor() > X_LOWER_BOUND + 10 and
            self.xcor() < X_UPPER_BOUND - 10):
            return True
        else:
            return False


    def hashitbottomwall(self):
        if (self.ycor() < Y_LOWER_BOUND and
            self.xcor() > X_LOWER_BOUND + 10 and
            self.xcor() < X_UPPER_BOUND - 10):
            return True
        else:
            return False


    def hashitpaddle(self, paddlex, paddletopy, paddlebottomy):
#        if paddlex == 460: # right paddle
#            print(paddlex, paddletopy, paddlebottomy)
        if (self.xcor() >= paddlex - 10 and
            self.xcor() <= paddlex + 10 and
            self.ycor() < paddletopy + 10 and
            self.ycor() > paddlebottomy + 10):
            return True
        else:
            return False


    def bounce(self, surface, direction):
        if surface == SURFACE_TOP and direction == DIRECTION_UP_LEFT:
            self.setheading(HEADING_DOWN_LEFT)
            self.direction = DIRECTION_DOWN_LEFT
        elif surface == SURFACE_TOP and direction == DIRECTION_UP_RIGHT:
            self.setheading(HEADING_DOWN_RIGHT)
            self.direction = DIRECTION_DOWN_RIGHT
        elif surface == SURFACE_BOTTOM and direction == DIRECTION_DOWN_LEFT:
            self.setheading(HEADING_UP_LEFT)
            self.direction = DIRECTION_UP_LEFT
        elif surface == SURFACE_BOTTOM and direction == DIRECTION_DOWN_RIGHT:
            self.setheading(HEADING_UP_RIGHT)
            self.direction = DIRECTION_UP_RIGHT
        elif surface == SURFACE_LEFT and direction == DIRECTION_UP_LEFT:
            self.setheading(HEADING_UP_RIGHT)
            self.direction = DIRECTION_UP_RIGHT
        elif surface == SURFACE_LEFT and direction == DIRECTION_DOWN_LEFT:
            self.setheading(HEADING_DOWN_RIGHT)
            self.direction = DIRECTION_DOWN_RIGHT
        elif surface == SURFACE_RIGHT and direction == DIRECTION_UP_RIGHT:
            self.setheading(HEADING_UP_LEFT)
            self.direction = DIRECTION_UP_LEFT
        else: # surface == SURFACE_RIGHT and direction == DIRECTION_DOWN_RIGHT
            self.setheading(HEADING_DOWN_LEFT)
            self.direction = DIRECTION_DOWN_LEFT
                