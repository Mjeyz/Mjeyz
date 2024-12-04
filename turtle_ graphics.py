from turtle import Turtle, Screen, colormode
import random

# Initialize the turtle and screen
timmy = Turtle()
timmy.speed("fastest")


# Function to generate random colors
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

for _ in range(100):
    timmy.color(random_colors())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)

# Keep the screen open
screen = Screen()
screen.mainloop()
