import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Random Walk")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
screen.bgcolor("black")

t.speed(0)  # Fastest speed
t.pensize(10)  # Set default line thickness

# Define colors
colors = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan"]


# Random walk function
def random_walk(steps):
    for _ in range(steps):
        # Choose a random color
        t.color(random.choice(colors))

        # Move in a random direction
        t.setheading(random.choice([0, 90, 180, 270]))  # 0°, 90°, 180°, 270°
        t.forward(30)  # Move forward by a fixed step


# Perform random walk
random_walk(100)

# Finish up
t.hideturtle()
screen.mainloop()
