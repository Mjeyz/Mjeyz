import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Dotted Line Example")

# Create a turtle
t = turtle.Turtle()
t.speed(5)  # Adjust speed (1 to 10 or 0 for max speed)

# Draw a dotted line
for _ in range(10):  # Change range for a longer line
    t.pendown()  # Start drawing
    t.forward(10)  # Draw a short line
    t.penup()  # Stop drawing
    t.forward(10)  # Move without drawing

# Finish up
t.hideturtle()  # Hide the turtle
screen.mainloop()  # Keep the window open

