
from turtle import Turtle, Screen
import colorgram
import random   
import turtle


colors = colorgram.extract('C:/Python Cursos/100 Days of Code The Complete Python Pro Bootcamp/day16_to_day20/day18/hirst_painting/image.jpg', 100)

def color_generator(colors):
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors

color_list = color_generator(colors)

"""Create spot paiting: 
10x10 rowls of spots / dot size: 20 / space: 50"""

def hirst_painting(the_turtle, color_list):
    the_turtle.speed("fastest")
    turtle.colormode(255)
    the_turtle.penup()
    the_turtle.hideturtle()
    the_turtle.goto(-250, -250)
    the_turtle.setheading(0)

    position = -250

    for times in range (10):
        for _ in range (10):
            selected_color = color_list[random.randint(0, len(color_list)-1)]
            the_turtle.color(selected_color)
            the_turtle.dot(20, selected_color)
            the_turtle.forward(50)

        position += 50
        the_turtle.goto(-250, position)




timmy = Turtle()
hirst_painting(timmy, color_list)

screen = Screen()
screen.exitonclick()