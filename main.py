from turtle import Turtle, Screen

# Create a turtle object
tim = Turtle()

# Define functions to move the turtle
def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
# Set up the screen
screen = Screen()
screen.listen()

# Bind keys to functions
screen.onkey(move_forward, key="w")  # Move forward with 'W' key
screen.onkey(move_backward, key="s")  # Move backward with 'S' key
screen.onkey(turn_left, key="s")
screen.onkey(turn_right, key="s")

# Close the screen on click
screen.exitonclick()
