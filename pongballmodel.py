from turtle import Turtle

X_UPPER_BOUND = 480
X_LOWER_BOUND = -480
Y_UPPER_BOUND = 280
Y_LOWER_BOUND = -280
XY_INCREMENT = 10
PADDLE_EDGE_ADJ = 10
SIDE_LEFT = "left"
SIDE_RIGHT = "right"


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.move_speed = 0.05
        self.incrementy = XY_INCREMENT
        self.incrementx = XY_INCREMENT


    def hashittopwall(self):
        if self.ycor() > Y_UPPER_BOUND:
            return True
        else:
            return False


    def hashitbottomwall(self):
        if self.ycor() < Y_LOWER_BOUND:
            return True
        else:
            return False


    def hashitleftwall(self):
        if self.xcor() < X_LOWER_BOUND:
            return True
        else:
            return False

    
    def hashitrightwall(self):
        if self.xcor() > X_UPPER_BOUND:
            return True
        else:
            return False


    def hashitpaddle(self, paddleside, paddlex, paddletopy, paddlebottomy):
        if (self.ycor() < paddletopy and
            self.ycor() > paddlebottomy):
            if (paddleside == SIDE_LEFT and
                self.xcor() < paddlex + PADDLE_EDGE_ADJ):
                return True
            elif (paddleside == SIDE_RIGHT and
                  self.xcor() > paddlex - PADDLE_EDGE_ADJ):
                return True
            else:
                return False


    def move(self):
        newx = self.xcor() + self.incrementx
        newy = self.ycor() + self.incrementy
        self.goto(newx, newy)


    def bouncex(self):
        self.incrementx *= -1


    def bouncey(self):
        self.incrementy *= -1


    def reset(self):
        self.goto(0, 0)
        self.bouncex()                