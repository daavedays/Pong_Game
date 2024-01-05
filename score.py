from turtle import Turtle

FONT = "Courier", 50, "normal"


class Scores(Turtle):
    """Turtle Class inheritance, used to create and update the scores as turtle objects."""
    def __init__(self) -> None:
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()

    def update_left_score(self):
        """Updates the left players score and makes the instance go to the specified location"""
        self.clear()
        self.left_score += 1
        self.goto(-200, 230)
        self.write(arg=self.left_score, align="center", font=FONT)

    def update_right_score(self):
        """Updates the right players score and makes the instance go to the specified location"""
        self.clear()
        self.right_score += 1
        self.goto(200, 230)
        self.write(arg=self.right_score, align="center", font=FONT)

