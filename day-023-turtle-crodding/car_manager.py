from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.number_of_cars = 20
        self.speed = STARTING_MOVE_DISTANCE
        for _ in range(self.number_of_cars):
            self.create_car()

    def manage_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.cars.remove(car)
                car.hideturtle()
                del car
                self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(-90)
        new_car.color(choice(COLORS))
        new_car.goto(randint(300, 1000), randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
