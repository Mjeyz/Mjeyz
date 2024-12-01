from turtle import Turtle, Screen

# Create a turtle instance
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

# Draw a triangle
timmy.forward(400)
timmy.left(120)
timmy.forward(400)
timmy.home()  # Corrected with parentheses

# Create a screen instance
my_screen = Screen()
print(my_screen.canvheight)  # Prints canvas height

# Close the window on click
my_screen.exitonclick()  # Corrected with parentheses

# Print the turtle object
print(timmy)
