from turtle import Screen
from paddles import Paddle
from divider import Divider
from time import sleep

# Screen Seteup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle((350, 0))   
paddle_left = Paddle((-350, 0))
divider = Divider()   

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

# Game main loop
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.05)
    paddle_right.move()
    paddle_left.move()

    # Detect collision with wall.
    if paddle_right.ycor() > 260 or paddle_right.ycor() < -260:
        paddle_right.direction = "stop"

    elif paddle_left.ycor() > 260 or paddle_left.ycor() < -260:
        paddle_left.direction = "stop"

    else:
        continue


screen.exitonclick()

