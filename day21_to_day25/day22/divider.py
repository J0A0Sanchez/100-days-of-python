from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        self.draw()

    def draw(self):
        while self.ycor() > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(15)