import time
from turtle import Screen
from turtlecrosscarmanager import CarManager
from turtlecrosspturtlemodel import PTurtle
from turtlecrossscoreboardmodel import Scoreboard


DIFFICULTY_HARD = 20
DIFFICULTY_NORMAL = 40
DIFFICULTY_EASY = 60


# instantiate objects
screen = Screen()

# initial object settings
screen.setup(width=1000, height=600)
screen.title("Turtle Cross")
screen.tracer(0)

# setup game
carmanager = CarManager()
carmanager.difficulty = DIFFICULTY_NORMAL
poneturtle = PTurtle()
scoreboard = Scoreboard()

# listen for keys
screen.listen()
screen.onkey(key="w", fun=poneturtle.moveforward)

# play game
gameover = False
while gameover == False:
    screen.update()
    time.sleep(0.1)
    
    # detect if turtle has been hit by a car
    for car in carmanager.cars:
        if poneturtle.lane == car.lane:
            if (car.x >= -15 and
                car.x <= 15):
                gameover = True

    # move cars
    carmanager.movecars()

    # detect if turtle has crossed successfully
    if poneturtle.isacrossfinishline() == True:
        scoreboard.addpoint()
        poneturtle.movetostart()
        carmanager.carsallowedperlane += 1
        carmanager.nextlevel()

# let players know game is over
scoreboard.gameover()

screen.exitonclick()