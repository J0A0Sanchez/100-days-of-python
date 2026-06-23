from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

# Onkey 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main loop: game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
    or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        screen.update()
        time.sleep(2)
        score.resetgame()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            score.game_over()
            screen.update()
            time.sleep(2)
            score.resetgame()
            snake.reset()

# Stop game
screen.exitonclick()