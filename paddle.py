from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):  # Position parameter is a tuple with co-ordinates for the locations of each instance.
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
