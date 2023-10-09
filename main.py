from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(n=0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')

screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Left')
screen.onkey(snake.left, 'Right')
screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    # detect collision with food.

    if snake.head.distance(food) < 15:
        print('nom nom nom')
        food.refresh()
        scoreboard.score_refresh()
        snake.extend()

    # detect collision with Wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        scoreboard.high_score_update()
        game_is_on = False


    # detect collision with tail.

    snake_body = snake.current_snake[1:]
    for segment in snake_body:
        #if segment == snake.head:
        #    pass
        if snake.head.distance(segment) < 10:
            print('collision with tail')
            scoreboard.game_over()
            scoreboard.high_score_update()
            game_is_on = False

screen.exitonclick()
