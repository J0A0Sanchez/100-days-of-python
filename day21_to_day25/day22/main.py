from turtle import Screen
from paddles import Paddle
from divider import Divider
from ball import Ball
from time import sleep
from turtle import Turtle

# ── Scoreboard ────────────────────────────────────────────────────────────────
score_left = 0
score_right = 0

scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()

def update_score():
    scoreboard.clear()
    scoreboard.goto(-100, 250)
    scoreboard.write(score_left, align="center", font=("Courier", 40, "normal"))
    scoreboard.goto(100, 250)
    scoreboard.write(score_right, align="center", font=("Courier", 40, "normal"))

# ── Screen Setup ──────────────────────────────────────────────────────────────
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
divider = Divider()
update_score()

# ── Controls ──────────────────────────────────────────────────────────────────
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

# ── Game main loop ────────────────────────────────────────────────────────────
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.05)
    paddle_right.move()
    paddle_left.move()
    ball.move_ball()

    # Paddle collision with top/bottom wall — stop
    if paddle_right.ycor() > 240 or paddle_right.ycor() < -240:
        paddle_right.direction = "stop"
    if paddle_left.ycor() > 240 or paddle_left.ycor() < -240:
        paddle_left.direction = "stop"

    # Ball bounce off top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball bounce off paddles
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50:
        ball.bounce_x()
    if ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.bounce_x()

    # Ball goes past right paddle — left scores
    if ball.xcor() > 390:
        score_left += 1
        update_score()
        ball.goto(0, 0)
        ball.bounce_x()

    # Ball goes past left paddle — right scores
    if ball.xcor() < -390:
        score_right += 1
        update_score()
        ball.goto(0, 0)
        ball.bounce_x()

screen.exitonclick()
