import turtle
from shape_factory import draw_polygon
import random

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(50, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)


def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    base = radius // 5
    t.penup()
    t.goto(x+(base // 2), y+2*(.99*radius))
    t.pendown()

    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(base)
    t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()



"""PUT YOUR FUNCTIONS HERE"""

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

#draw_pumpkin(t, 0, -100, 100)  # Draw the pumpkin
#draw_eye(t, -40, 0, 30)  # Left eye
#draw_eye(t, 40, 0, 30)   # Right eye
#draw_mouth(t, -50, -50, 100)  # Mouth

# Draw three jack-o-lanterns
draw_pumpkin(t, -150, -250, 100)
draw_eye(t, -190, -160, 30)  # Left eye
draw_eye(t, -110, -160, 30)  # Right eye
draw_mouth(t, -190, -200, 80)  # Mouth

draw_pumpkin(t, 0, -250, 80)
draw_eye(t, -20, -170, 25)
draw_eye(t, 20, -170, 25)
draw_mouth(t, -30, -210, 60)

draw_pumpkin(t, 150, -250, 100)
draw_eye(t, 110, -160, 30)
draw_eye(t, 190, -160, 30)
draw_mouth(t, 110, -200, 80)

# Draw the night sky
draw_sky(t, 30)

# Close the turtle graphics window when clicked
turtle.exitonclick()
