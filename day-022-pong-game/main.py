from turtle import Screen
from paddle import Paddle, PaddlePostion
from boundary import Boundary
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.title(titlestring='Pong')
screen.setup(width=820, height=620)
paddle1 = Paddle(PaddlePostion.LEFT)
paddle2 = Paddle(PaddlePostion.RIGHT)
boundary = Boundary()
ball = Ball()

screen.update()

screen.listen()
screen.onkeypress(paddle1.move_up, 'w')
screen.onkeypress(paddle1.move_down, 's')
screen.onkeypress(paddle2.move_up, 'Up')
screen.onkeypress(paddle2.move_down, 'Down')

is_game_on = True
while is_game_on:
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    screen.update()

screen.exitonclick()
