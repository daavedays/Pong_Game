from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.dx = 3
        self.dy = 3
        self.ball_speed = 0.005

    def initiate_motion(self):
        """We create a new x and y position for the ball to keep moving towards."""
        new_x = (self.xcor() + self.dx)
        new_y = (self.ycor() + self.dy)
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Changes the direction of travel on the Y-axis."""
        self.dy *= -1

    def bounce_x(self):
        """Changes the direction of travel on X-axis."""
        self.dx *= -1
        self.ball_speed *= 0.2

    def reset_ball(self):
        """Resets the position of the ball and updates the ball speed."""
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.005

