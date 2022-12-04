from turtle import Screen
from snake import Snake


screen = Screen()
snake_player = Snake(screen)
# screen = GameScreen(snake_player.up, snake_player.down,
#                     snake_player.left, snake_player.right)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)
screen.onkeypress(snake_player.up, "Up")
screen.onkeypress(snake_player.down, "Down")
screen.onkeypress(snake_player.left, "Left")
screen.onkeypress(snake_player.right, "Right")

screen.update()

game_is_on = True

while game_is_on:
    screen.ontimer(snake_player.move(), 100)

screen.exitGame()
