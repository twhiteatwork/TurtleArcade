import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0


class Snake:
    

    def __init__(self):
        self.bodyparts = []
        self.heading = 0
        self.create()
        self.head = self.bodyparts[0]


    def create(self):
        for position in STARTING_POSITIONS:
            self.addbodypart(position)


    def addbodypart(self, position):
        newbodypart = t.Turtle("square")
        newbodypart.color("white")
        newbodypart.penup()
        newbodypart.goto(position)
        self.bodyparts.append(newbodypart)


    def extend(self):
        tail = self.bodyparts[len(self.bodyparts) - 1]
        newbodypartposition = (tail.xcor(), tail.ycor())
        self.addbodypart(newbodypartposition)


    def move(self):
        for bodypartindex in range(len(self.bodyparts) - 1, 0, -1):
            bodypartgotox = self.bodyparts[bodypartindex - 1].xcor()
            bodypartgotoy = self.bodyparts[bodypartindex - 1].ycor()
            self.bodyparts[bodypartindex].goto(bodypartgotox, bodypartgotoy)
        self.bodyparts[0].setheading(self.heading)
        self.bodyparts[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.heading != HEADING_DOWN:
            self.heading = HEADING_UP


    def down(self):
        if self.heading != HEADING_UP:
            self.heading = HEADING_DOWN


    def left(self):
        if self.heading != HEADING_RIGHT:
            self.heading = HEADING_LEFT


    def right(self):
        if self.heading != HEADING_LEFT:
            self.heading = HEADING_RIGHT
    

    def hashitwall(self):
        if (self.head.xcor() > 280 or
            self.head.xcor() < -280 or
            self.head.ycor() > 280 or
            self.head.ycor() < -280):
            return True
        else:
            return False


    def hashittail(self):
        # must exclude snake head from check
        for bodypart in self.bodyparts[1:]:
            if self.head.distance(bodypart) < 10:
                return True
        return False