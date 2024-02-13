import time
from turtle import Screen
from snakemodel import Snake
from snakefoodmodel import Food
from snakescoreboardmodel import Scoreboard


# instantiate objects
screen = Screen()

# initial object settings
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# setup game
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listen for keys
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)

# play game
gameover = False
while gameover == False:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect snake head has touched food
    # extend snake
    # move food
    # update score
    if snake.head.distance(food) < 15:
        snake.extend()
        food.move()
        scoreboard.addpoint()
        scoreboard.update()
    
    # detect snake head has touched a wall
    if snake.hashitwall() == True:
        gameover = True
    
    # detect snake head has touched its tail
    if snake.hashittail() == True:
        gameover = True

scoreboard.gameover()

screen.exitonclick()