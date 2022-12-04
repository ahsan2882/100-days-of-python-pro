from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from difficulty import Difficulty


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
user_diff = screen.textinput(
    title="Choose difficulty", prompt="Easy, Medium, Hard")
snake_player = Snake(screen=screen, difficulty=user_diff)
food = Food(screen)
score_manager = Scoreboard()
screen.listen()
screen.onkeypress(snake_player.up, "Up")
screen.onkeypress(snake_player.down, "Down")
screen.onkeypress(snake_player.left, "Left")
screen.onkeypress(snake_player.right, "Right")

screen.update()

game_is_on = True
speed = 800
boundaryX = (screen.window_width() / 2) - 20
boundaryY = (screen.window_height() / 2) - 20

if user_diff.lower() == Difficulty.MEDIUM.value:
    speed = 500
elif user_diff.lower() == Difficulty.HARD.value:
    speed = 200

while game_is_on:
    screen.update()
    screen.ontimer(snake_player.move(), speed)
    if snake_player.head.distance(food.pos()) < 15:
        food.refresh()
        snake_player.extend()
        score_manager.increase_score()

    if user_diff.lower() == Difficulty.MEDIUM.value or user_diff.lower() == Difficulty.HARD.value:
        if snake_player.head.xcor() > boundaryX or snake_player.head.xcor() < -boundaryX or snake_player.head.ycor() > boundaryY or snake_player.head.ycor() < -boundaryY:
            game_is_on = False
            score_manager.game_over()

screen.exitonclick()
