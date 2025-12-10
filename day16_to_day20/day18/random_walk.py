from turtle import Turtle, Screen
import random
import turtle


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk(turtle, time):
    step = 30
    directions = [0, 90, 180, 270]

    turtle.shape("circle")
    turtle.pensize(10)
    turtle.speed("fastest")

    for _ in range(time):
        turtle.setheading(random.choice(directions))
        turtle.forward(step)

        color = random_color()
        turtle.color(color)




timmy = Turtle()
turtle.colormode(255)
random_walk(timmy, 100)

screen = Screen()
screen.exitonclick()



