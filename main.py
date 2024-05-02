import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')

screen.tracer(0)
game_is_on = True
screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 12:
        food.refresh()
        scoreboard.increment()

        #add segment witih the snake
        snake.extends()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) <9:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()