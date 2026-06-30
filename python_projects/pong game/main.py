import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
left_scoreboard = Scoreboard((-150, 230))
right_scoreboard = Scoreboard((150, 230))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)  # Refresh time
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
        ball.increase_speed()

    # Detect when the ball misses the right paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        left_scoreboard.increase_score()

    # Detect when the ball misses the left paddle
    if ball.xcor() < -380:
        ball.reset_ball()
        right_scoreboard.increase_score()

screen.exitonclick()
