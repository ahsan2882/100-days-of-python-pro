from turtle import Screen
from snake import Snake
from difficulty import Difficulty


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
user_diff = screen.textinput(
    title="Choose difficulty", prompt="Easy, Medium, Hard")
print(user_diff)
snake_player = Snake(screen=screen, difficulty=user_diff)
screen.listen()
screen.onkeypress(snake_player.up, "Up")
screen.onkeypress(snake_player.down, "Down")
screen.onkeypress(snake_player.left, "Left")
screen.onkeypress(snake_player.right, "Right")

screen.update()

game_is_on = True
speed = 800
if user_diff.lower() == Difficulty.MEDIUM.value:
    speed = 500
elif user_diff.lower() == Difficulty.HARD.value:
    speed = 200

while game_is_on:
    screen.update()
    screen.ontimer(snake_player.move(), speed)

screen.exitGame()
