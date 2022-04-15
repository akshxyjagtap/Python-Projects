from turtle import Turtle
import random
FOOD_COLOR = "green"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.shapesize(stretch_len=0.7, stretch_wid= 0.7)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.new()
    def new(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)

