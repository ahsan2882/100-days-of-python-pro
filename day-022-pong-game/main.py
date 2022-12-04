from turtle import Screen
from paddle import Paddle, PaddlePostion
from boundary import Boundary
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.title(titlestring='Pong')
screen.setup(width=820, height=620)
boundary = Boundary()
ball = Ball()
paddle1 = Paddle(PaddlePostion.LEFT)
paddle2 = Paddle(PaddlePostion.RIGHT)

screen.update()

screen.listen()
screen.onkeypress(paddle1.move_up, 'w')
screen.onkeypress(paddle1.move_down, 's')
screen.onkeypress(paddle2.move_up, 'Up')
screen.onkeypress(paddle2.move_down, 'Down')

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
