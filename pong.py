import time
from turtle import Screen
from pongballmodel import Ball
from pongpaddlemodel import Paddle
from pongscoreboardmodel import Scoreboard


WINNING_SCORE = 7


# instantiate objects
screen = Screen()

# initial object settings
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# setup game
leftpaddle = Paddle("left")
rightpaddle = Paddle("right")
leftscoreboard = Scoreboard("left")
rightscorboard = Scoreboard("right")
gameoverscoreboard = Scoreboard("none")
ball = Ball()

# listen for keys
screen.listen()
screen.onkey(key="w", fun=leftpaddle.up)
screen.onkey(key="s", fun=leftpaddle.down)
screen.onkey(key="Up", fun=rightpaddle.up)
screen.onkey(key="Down", fun=rightpaddle.down)

# play game
gameover = False
while gameover == False:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect if ball has hit top wall
    if ball.hashittopwall() == True:
        ball.bouncey()

    # detect if ball has hit bottom wall
    if ball.hashitbottomwall() == True:
        ball.bouncey()

    # detect if ball has hit left wall
    if ball.hashitleftwall() == True:
        rightscorboard.addpoint()
        ball.reset()

    # detect if ball has hit right wall
    if ball.hashitrightwall() == True:
        leftscoreboard.addpoint()
        ball.reset()

    # detect if ball has hit leftpaddle
    if ball.hashitpaddle(leftpaddle.side, leftpaddle.x, leftpaddle.topy, leftpaddle.bottomy):
        ball.bouncex()

    # detect if ball has hit rightpaddle
    if ball.hashitpaddle(rightpaddle.side, rightpaddle.x, rightpaddle.topy, rightpaddle.bottomy):
        ball.bouncex()


    # detect if a player score has exceeded 7 and end game
    if leftscoreboard.score == WINNING_SCORE or rightscorboard.score == WINNING_SCORE:
        gameover = True

# let players know game is over
gameoverscoreboard.gameover()

screen.exitonclick()