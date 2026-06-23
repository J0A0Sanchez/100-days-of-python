from turtle import Turtle

class Ball(Turtle):
    def __ini__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

