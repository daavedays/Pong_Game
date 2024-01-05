from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scores
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong2")
screen.setup(800, 600)
screen.tracer(0)

border = Turtle()
border.color("white")
border.hideturtle()
border.penup()
border.goto(x=0, y=-300)
border.left(90)
border.pensize(4)
for i in range(40):  # Draws the border.
    border.pendown()
    border.forward(10)
    border.penup()
    border.forward(10)

paddle1 = Paddle(position=(350, 0))
paddle2 = Paddle(position=(-350, 0))

score_right = Scores()
score_left = Scores()

ball = Ball()

screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

game_on = True
while game_on:
    """Main game logic where the collisions with the walls and paddles are handled."""
    screen.update()
    ball.initiate_motion()
    time.sleep(ball.ball_speed)

    # Collision with the top and bottom borders.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collisions with the players' paddles.
    if ((330 < ball.xcor() < 350 and paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50)
            or ball.distance(paddle1) < 20
            or (-350 < ball.xcor() < -330 and (paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50))
            or ball.distance(paddle2) < 20):
        ball.bounce_x()

    # Ball missing the right paddle.
    if ball.xcor() > 400:
        score_left.update_left_score()
        ball.reset_ball()
        ball.initiate_motion()

    # Ball missing the left paddle.
    if ball.xcor() < -400:
        score_right.update_right_score()
        ball.reset_ball()
        ball.initiate_motion()

