from turtle import Screen
from paddle import Paddle, PaddlePostion
from boundary import Boundary
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.mode('logo')
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
player1_score = 0
player2_score = 0
scoreboard = Scoreboard()


def hit_paddle(paddle) -> bool:
    for paddle_segment in paddle.paddle:
        if ball.distance(paddle_segment) < 23:
            ball.increase_speed()
            return True
    return False


is_game_on = True
while is_game_on:
    ball.move()
    [xcor, ycor] = ball.position()
    heading = ball.heading()
    if ycor > 280:
        if heading > 0 and heading < 90:
            ball.bounce(180-heading)
        elif heading > 270 and heading < 360:
            ball.bounce(540-heading)
    elif ycor < -280:
        if heading > 180 and heading < 270:
            ball.bounce(540-heading)
        elif heading > 90 and heading < 180:
            ball.bounce(180-heading)

    if (-331 < xcor < -329):
        if hit_paddle(paddle1):
            ball.bounce(360-heading)

    elif (xcor < -380 and not hit_paddle(paddle1)):
        player2_score += 1
        ball.reset()
        scoreboard.update_scoreboard(player1_score, player2_score)

    elif (329 < xcor < 331):
        if hit_paddle(paddle2):
            ball.bounce(360-heading)

    elif (xcor > 380 and not hit_paddle(paddle2)):
        player1_score += 1
        ball.reset()
        scoreboard.update_scoreboard(player1_score, player2_score)

    screen.update()

screen.exitonclick()
