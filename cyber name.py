import turtle
import random

# Set up the screen
turtle.bgcolor("grey")  # Background color

# Decide colors for depth illusion
colors = ['magenta', 'blue', 'indigo', 'yellow']

# Set up the turtle for drawing text
turtle.pensize(5)
turtle.speed(0)  # Fastest drawing speed for the background

# Function to draw 1s and 0s in the background
def draw_background():
    turtle.penup()
    turtle.color("lime green")  # Change color to lime green
    for _ in range(100):  # Draw 100 random 1s and 0s
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        turtle.goto(x, y)
        turtle.write(random.choice(['1', '0']), font=("Arial", 16, "bold"))  # Increase font size

# Function to draw text with a depth illusion
def draw_depth_text(text, x, y):
    for offset in range(5):  # Create layers for depth effect
        turtle.penup()
        turtle.goto(x - offset * 10, y - offset * 10 )  # Slightly adjust y for layering
        turtle.pendown()
        for i, char in enumerate(text):
            # Set color and font size
            turtle.pencolor(colors[i % len(colors)])  
            turtle.write(char, font=("Arial", 36, "bold"))  # Use the same font size
            turtle.penup()
            turtle.forward(40)  # Space between letters
            turtle.pendown()

# Draw the background
draw_background()

# Draw the name "Cyber Hank"
draw_depth_text("Cyber Hank", -100, 0)

# Finish up
turtle.hideturtle()
turtle.done()
