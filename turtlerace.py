import turtle as t
import random

def movetforwardrandomly(t):
    t.forward(random.randint(0,10))

def thaswon(t):
    if t.xcor() > 100:
        return True
    else:
        return False

# instantiate objects
tred = t.Turtle(shape="turtle")
tgreen = t.Turtle(shape="turtle")
tblue = t.Turtle(shape="turtle")
screen = t.Screen()

# object settings
screen.setup(width=500, height=400)
tred.color("red")
tgreen.color("green")
tblue.color("blue")
tred.speed("fastest")
tgreen.speed("fastest")
tblue.speed("fastest")
tred.penup()
tgreen.penup()
tblue.penup()

# race
# send turtles to starting line at x = -230
tred.goto(x=-230, y=100)
tgreen.goto(x=-230, y=50)
tblue.goto(x=-230, y=0)

# gather user bet
bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win red, green or blue? ")

# move turtles forward randomly until one has crossed the finish line, x = 100
raceover = False
winner = "Undetermined"
while raceover == False:
    movetforwardrandomly(tred)
    movetforwardrandomly(tgreen)
    movetforwardrandomly(tblue)
    if thaswon(tred) == True:
        winner = "red"
        tred.write("Winner")
        raceover = True
    if thaswon(tgreen) == True:
        winner = "green"
        tgreen.write("Winner")
        raceover = True
    if thaswon(tblue) == True:
        winner = "blue"
        tblue.write("Winner")
        raceover = True

# output bet result
if bet == winner:
    print("You bet correctly!")
else:
    print("You bet incorrectly")

screen.exitonclick()