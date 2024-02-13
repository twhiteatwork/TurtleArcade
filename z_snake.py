import turtle as t
import random
import time


def movesnakeforward():
    xsnakebodypartparent = snakehead.xcor()
    ysnakebodypartparent = snakehead.ycor()
    headingsnakebodypartparent = snakehead.heading()
    snakehead.forward(20)
    for snakebodypart in snakebody:
        xgoto = xsnakebodypartparent
        ygoto = ysnakebodypartparent
        newheading = headingsnakebodypartparent
        xsnakebodypartparent = snakebodypart.xcor()
        ysnakebodypartparent = snakebodypart.ycor()
        headingsnakebodypartparent = snakebodypart.heading()
        snakebodypart.goto(xgoto, ygoto)
        snakebodypart.setheading(newheading)
    screen.update()

def turnsnakeleft():
    snakehead.left(90)


def turnsnakeright():
    snakehead.right(90)


def addsnakebodypart(xoffsetfromsnakehead):
    snakebodypart = t.Turtle(shape="square")
    snakebodypart.color("white")
    snakebodypart.penup()
    snakebodypart.goto(xoffsetfromsnakehead, 0)
    snakebody.append(snakebodypart)


def placefoodpellet():
    xoptions = []
    yoptions = []
    for x in range(-260, 261, 20):
        xoptions.append(x)
    for y in range(-260, 261, 20):
        yoptions.append(y)
    xgoto = random.randint(0, len(xoptions) + 1)
    ygoto = random.randint(0, len(yoptions) + 1)
    foodpellet.goto(xgoto, ygoto)
    screen.update()


def eatfoodpellet():
    playerscorescore += 1
    placefoodpellet()
    screen.update()


def issnakeheadatfoodpellet():
    if (snakehead.xcor() == foodpellet.xcor() and
        snakehead.ycor() == foodpellet.ycor()):
        return True
    else:
        return False


snakebody = []

# instantiate objects
snakehead = t.Turtle(shape="square")
snaketail = t.Turtle(shape="square")
foodpellet = t.Turtle(shape="square")
screen = t.Screen()

# initial object settings
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snakehead.color("white")
snakehead.penup()
snaketail.hideturtle()
snaketail.penup()
foodpellet.color("red")
foodpellet.penup()

# setup game
playerscore = 0
placefoodpellet()
addsnakebodypart(-20)
addsnakebodypart(-40)
screen.update()

# listen for keys
screen.listen()
screen.onkey(key="w", fun=movesnakeforward)
screen.onkey(key="a", fun=turnsnakeleft)
screen.onkey(key="d", fun=turnsnakeright)

gameover = False
while gameover == False:
    time.sleep(0.1)
    movesnakeforward()
    if issnakeheadatfoodpellet():
        eatfoodpellet()
    if (snakehead.xcor() == -280 or
        snakehead.xcor() == 280 or
        snakehead.ycor() == -280 or
        snakehead.ycor() == 280):
        gameover = True

# listen for keys
screen.listen()
screen.onkey(key="w", fun=movesnakeforward)
screen.onkey(key="a", fun=turnsnakeleft)
screen.onkey(key="d", fun=turnsnakeright)

screen.exitonclick()