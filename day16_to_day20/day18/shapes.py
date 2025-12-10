from turtle import Turtle, Screen
import random

dark_colors = [
    "black",
    "dark slate gray",
    "dim gray",
    "slate gray",
    "midnight blue",
    "navy",
    "cornflower blue",
    "dark slate blue",
    "slate blue",
    "medium slate blue",
    "medium blue",
    "royal blue",
    "blue",
    "dark turquoise",
    "cadet blue",
    "dark green",
    "dark olive green",
    "sea green",
    "forest green",
    "olive drab",
    "dark khaki",
    "dark goldenrod",
    "rosy brown",
    "indian red",
    "saddle brown",
    "sandy brown",
    "dark salmon",
    "dark orange",
    "tomato",
    "orange red",
    "red",
    "hot pink",
    "deep pink",
    "pale violet red",
    "maroon",
    "medium violet red",
    "violet red",
    "medium orchid",
    "dark orchid",
    "dark violet",
    "blue violet",
    "purple",
    "medium purple"
]

timmy = Turtle()

#timmy.shape("turtle")

count = 3
angle = 360

while count < 10:
    for steps in range (0, count):
        timmy.forward(100)
        timmy.right(angle / count)
        

    count += 1
    color = random.choice(dark_colors)
    timmy.color(color)



screen = Screen()
screen.exitonclick()