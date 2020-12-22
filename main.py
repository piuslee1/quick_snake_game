import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on=False
        scoreboard.game_over()
    #tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on=False
            scoreboard.game_over()

screen.exitonclick()
