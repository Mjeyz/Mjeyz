from turtle import Turtle, Screen
import random
from question_model import colors

timmy = Turtle()
timmy.pensize(10)

def draw_shape(steps):
    for num_steps in range(steps):
        timmy.color(random.choice(colors))

        timmy.setheading(random.choice([0, 90, 180, 270]))
        timmy.forward(30)



draw_shape(100)
screen = Screen()
screen.mainloop()
