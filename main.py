from turtle import Turtle, Screen

from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

game_is_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# stoop animation in the screen
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle((-350, 0))
l_paddle = Paddle((350, 0))
ball = Ball((0, 0))

time_laps = 0.1





# listing
screen.listen()
screen.onkeypress(l_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "s")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # tha cneter is one pixel
    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #  print("gana derecho")
    if ball.xcor() < - 380:
        scoreboard.r_point()
        ball.return_center()

    # gana derecho
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.return_center()

screen.exitonclick()
