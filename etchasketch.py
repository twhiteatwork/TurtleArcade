import turtle as t


def moveforward():
    turt.forward(10)


def movebackward():
    turt.backward(10)


def turnleft():
    turt.left(10)


def turnright():
    turt.right(10)


def clearscreen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


# instantiate objects
turt = t.Turtle()
screen = t.Screen()

# settings
turt.speed("fastest")

# listen for keys
screen.listen()
screen.onkey(key="w", fun=moveforward)
screen.onkey(key="b", fun=movebackward)
screen.onkey(key="a", fun=turnleft)
screen.onkey(key="d", fun=turnright)
screen.onkey(key="c", fun=clearscreen)

screen.exitonclick()