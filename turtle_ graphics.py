import turtle as t
import random

# Predefined color palette
color_list = [(244, 238, 230), (249, 229, 236), (240, 250, 244), (29, 41, 60), (49, 92, 143),
              (145, 81, 44), (170, 14, 28), (160, 56, 87), (227, 154, 8), (209, 162, 105),
              (235, 217, 75), (66, 30, 43), (236, 240, 246), (37, 142, 47), (222, 225, 4),
              (48, 36, 30), (46, 47, 96), (95, 193, 168), (120, 161, 172), (19, 54, 47),
              (243, 89, 22), (161, 16, 13), (18, 97, 45), (212, 58, 79), (49, 169, 80),
              (189, 146, 159), (231, 173, 186), (226, 177, 168), (45, 153, 195),
              (160, 212, 184), (74, 77, 43), (116, 122, 156)]

# Turtle setup
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
t.colormode(255)
tim.hideturtle()

# Starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Parameters for the grid
rows = 10
cols = 10
dot_size = 20
spacing = 50

# Draw grid
for row in range(rows):
    for col in range(cols):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(spacing)
    tim.forward(cols * spacing)  # Reset position to start of row
    tim.right(90)
    tim.forward(spacing)
    tim.left(90)

# Keep screen open
screen = t.Screen()
screen.exitonclick()
