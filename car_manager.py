from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        x = 300
        y = random.randint(-240, 240)
        if random.randint(1, 6) == 1:
            self.add_car((x, y))

    def add_car(self, position):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        car.goto(position)
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() <= -310:
                car.hideturtle()
                car.clear()

        self.cars = [car for car in self.cars if car.xcor() > -310]
    
    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def detect_collision_with_player(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

