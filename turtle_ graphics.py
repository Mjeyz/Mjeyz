from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")
colors = ["brown", "medium sea green", "dodger blue", "plum", "salmon", "goldenrod", "light slate gray", "gold"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for sides_shapes_n in range(3, 11):
    timmy.color(choice(colors))
    draw_shape(sides_shapes_n)


screen = Screen()
timmy.hideturtle()
screen.exitonclick()
