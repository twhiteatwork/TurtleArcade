import turtle as t

X_UPPER_BOUND = 460
X_LOWER_BOUND = -460
Y_UPPER_BOUND = 280
Y_LOWER_BOUND = -280
HEADING_UP = 90
HEADING_DOWN = 270
SIDE_LEFT = "left"
SIDE_RIGHT = "right"


class Paddle:


    def __init__(self, side):
        super().__init__()
        self.side = side
        self.x = 0
        self.segments = []
        self.create()
        self.topy = self.segments[0].ycor()
        self.bottomy = self.segments[len(self.segments) - 1].ycor()

    
    def create(self):
        if self.side == SIDE_LEFT:
            x = X_LOWER_BOUND
        else: # right
            x = X_UPPER_BOUND
        for y in range(40, -40, -20):
            position = (x, y)
            self.addsegment(position)
        self.x = x

    def addsegment(self, position):
        newsegment = t.Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)


    def up(self):
        if self.topy + 20 <= Y_UPPER_BOUND:
            for segment in self.segments:
                newsegmenty = segment.ycor() + 20
                segment.goto(self.x, newsegmenty)
            self.topy = self.segments[0].ycor()
            self.bottomy = self.segments[len(self.segments) - 1].ycor()


    def down(self):
        if self.bottomy - 20 >= Y_LOWER_BOUND:
            for segment in self.segments:
                newsegmenty = segment.ycor() - 20
                segment.goto(self.x, newsegmenty)
            self.topy = self.segments[0].ycor()
            self.bottomy = self.segments[len(self.segments) - 1].ycor()
