from turtle import Turtle
from difficulty import Difficulty

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self, screen, difficulty):
        self.snake_body = []
        self.screen = screen
        self.difficulty = difficulty
        self.turtle_position = (0, 0)
        self.head = self.create_snake()

    def create_snake(self):
        for i in range(8):
            snake = Turtle(shape="square")
            if i == 0:
                snake.color("red")
            else:
                snake.color("white")
            snake.penup()
            snake.goto(self.turtle_position)
            self.turtle_position = (
                self.turtle_position[0] - 20, self.turtle_position[1])
            self.snake_body.append(snake)
        return self.snake_body[0]

    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[seg_num].goto(self.snake_body[seg_num-1].pos())
        self.head.forward(20)
        if self.difficulty.lower() == Difficulty.EASY.value:
            if self.head.pos()[0] < ((self.screen.window_width()/2) - 30)*-1:
                self.head.goto(
                    (self.screen.window_width()/2) - 30,
                    self.head.pos()[1])
            elif self.head.pos()[0] > (self.screen.window_width()/2) - 30:
                self.head.goto(
                    ((self.screen.window_width()/2) - 30)*-
                    1, self.head.pos()[1]
                )
            elif self.head.pos()[1] < ((self.screen.window_height()/2)-30)*-1:
                self.head.goto(
                    self.head.pos()[0], (self.screen.window_height()/2)-30)
            elif self.head.pos()[1] > ((self.screen.window_height()/2)-30):
                self.head.goto(
                    self.head.pos()[0], ((self.screen.window_height()/2)-30)*-1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()
