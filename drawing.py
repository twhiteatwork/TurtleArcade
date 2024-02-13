import turtle as t
import random

TURTLECOLORS = ["dark blue", "forest green", "gold", "maroon", "magenta", "dark violet", "turquoise", "red", "black"]
DIRECTIONS = [0, 90, 180, 270]


# Return random RGB color as tuple
def randomcolor():
    color_r = random.randint(0, 255)
    color_g = random.randint(0, 255)
    color_b = random.randint(0, 255)
    return (color_r, color_g, color_b)


# Draw a multi sided shape
def drawshape(turt, sidelength, numsides):
    angle = 360 / numsides
    for _ in range(0, numsides):
        turt.forward(sidelength)
        turt.left(angle)


# Draw a square
def drawsquare(turt, sidelength):
    drawshape(turt, sidelength, 4)


# Draw a dashed line
def drawdashline(turt, linelength, dashlength):
    linelength -= (linelength % dashlength) #Trim off remainder
    turt.penup() #Start state
    for _ in range(0, linelength, dashlength):
        if turt.pen()["pendown"] == False:
            turt.pendown()
        else:
            turt.penup()
        turt.forward(dashlength)


# Draw random walk
def drawrandomwalk(turt, segmentdistance, numberofsegments):
    global TURTLECOLORS, DIRECTIONS
    for _ in range(0, numberofsegments + 1):
        turt.color(randomcolor())
        turt.setheading(random.choice(DIRECTIONS))
        turt.forward(segmentdistance)


# Draw a spirograph
def drawspirograph(turt, gapsize):
    for _ in range(int(360 / gapsize)):
        turt.color(randomcolor())
        turt.circle(100)
        turt.setheading(turt.heading() + gapsize)

# init turtle
turt = t.Turtle()
t.colormode(255)

# default turtle settings
turt.shape("turtle")
turt.color("black")
turt.pensize(15)
turt.speed("fastest")

# draw stuff
#drawshape(turt, 100, 5)
#drawsquare(turt, 100)
#drawdashline(turt, 100, 4)
#drawrandomwalk(turt, 30, 100)
drawspirograph(turt, 5)

# keep draw window open until closed by user
screen = t.Screen()
screen.exitonclick()
