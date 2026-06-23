from turtle import Turtle, Screen

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5) 
        self.setheading(90)  
        self.penup()
        self.goto(position)
        self.direction = "stop"

    def move(self):
        if self.direction == "up":
            self.goto(self.xcor(), self.ycor() + 20)
        elif self.direction == "down":
            self.goto(self.xcor(), self.ycor() - 20)

    def go_up(self):
        self.direction = "up"

    def go_down(self):
        self.direction = "down"