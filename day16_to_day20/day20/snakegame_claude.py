import turtle
import time
import random

# ── Setup ──────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # turn off auto-animation

# ── Create a snake body ────────────────────────────────────────────────────────
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

segments = []

def create_snake():
    for position in STARTING_POSITIONS:
        add_segment(position)

def add_segment(position):
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

create_snake()

# ── Create food ────────────────────────────────────────────────────────────────
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)

# ── Create a scoreboard ────────────────────────────────────────────────────────
score = 0
high_score = 0

scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 270)

def update_score():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}  High Score: {high_score}", align="center",
                     font=("Courier", 16, "normal"))

update_score()

# ── Move the snake ─────────────────────────────────────────────────────────────
def move():
    # move each segment to the position of the one ahead of it
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    # move the head forward
    segments[0].forward(MOVE_DISTANCE)

# ── Control the snake ──────────────────────────────────────────────────────────
def go_up():
    if segments[0].heading() != DOWN:
        segments[0].setheading(UP)

def go_down():
    if segments[0].heading() != UP:
        segments[0].setheading(DOWN)

def go_left():
    if segments[0].heading() != RIGHT:
        segments[0].setheading(LEFT)

def go_right():
    if segments[0].heading() != LEFT:
        segments[0].setheading(RIGHT)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# ── Reset game ─────────────────────────────────────────────────────────────────
def reset():
    global score
    time.sleep(1)
    for seg in segments:
        seg.goto(1000, 1000)  # move off screen
    segments.clear()
    create_snake()
    segments[0].setheading(RIGHT)
    score = 0
    update_score()

# ── Main game loop ─────────────────────────────────────────────────────────────
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move()

    # Detect collision with food
    if segments[0].distance(food) < 15:
        food.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
        add_segment(segments[-1].position())
        score += 1
        if score > high_score:
            high_score = score
        update_score()

    # Detect collision with wall
    if (segments[0].xcor() > 290 or segments[0].xcor() < -290
            or segments[0].ycor() > 290 or segments[0].ycor() < -290):
        reset()

    # Detect collision with tail
    for segment in segments[1:]:
        if segments[0].distance(segment) < 10:
            reset()

screen.mainloop()
