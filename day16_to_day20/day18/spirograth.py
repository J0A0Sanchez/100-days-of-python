from turtle import Turtle, Screen
import random
import turtle



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy = Turtle()
timmy.speed("fastest")
turtle.colormode(255)

angle = 0

for _ in range(73):
    color = random_color()
    timmy.color(color)
    timmy.circle(100)
    timmy.setheading(angle)  
    angle += 5



screen = Screen()
screen.exitonclick()