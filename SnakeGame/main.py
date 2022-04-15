from turtle import Screen, Turtle
import time
from scorebord import Scoreboard
from food import Food
from snake import Snake

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game - DSA Mini Project")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision w food
    if snake.head.distance(food) < 18:
        food.new()
        snake.extent()
        scoreboard.increase_score()

    # detect collision w wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on = False

    # detect collision w tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()

scoreboard.game_over()
screen.exitonclick()
