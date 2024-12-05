from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

# Ask for user's bet
turtle_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

# Define the turtle colors and y-positions
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create turtles and set their starting positions
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Simple race logic
if turtle_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in all_turtles:
        # Move each turtle forward a random distance
        turtle.forward(random.randint(0, 10))

        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == turtle_bet:
                print(f"Congratulations! The {winning_color} turtle won!")
            else:
                print(f"Sorry, the {winning_color} turtle won the race!")

screen.mainloop()
