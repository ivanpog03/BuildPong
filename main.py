from turtle import *
import time
import paddle
from ball import Ball
from paddle import *
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()

scoreboard=Scoreboard()
ball=Ball()
l_paddle = Paddle(350, 0)
r_paddle = Paddle(-350, 0)
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.speeed)
    screen.update()
    ball.move_to()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(l_paddle)<50 and ball.xcor()>320 or ball.distance(r_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        scoreboard.l_plus()
        ball.setpos(0,0)
        ball.bounce_x()
    elif ball.xcor()<-380:
        scoreboard.r_plus()
        ball.setpos(0,0)
        ball.bounce_x()



screen.exitonclick()
