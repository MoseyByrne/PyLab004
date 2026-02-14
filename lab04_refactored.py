""" NOTE:
I tried this on my own and got stumped, but I was able to find help
and someone to talk me through it. There are lots of notes
so I can look back and remember how/why we did things.
"""

import turtle
from shape_factory import draw_polygon

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin with a stem, 2 triangular eyes, and a zigzag mouth.
    NOTE: x,y is the circle start point (bottom of the pumpkin), not the center.
    """

    def filled_at(x0, y0, color, draw_fn): # using x0, y0 instead of x, y to avoid variable shadowing. Would handle the same, but helps readability
        t.penup() # lifts the turtle up
        t.goto(x0, y0) # goes to the x and y coordinates
        t.pendown() # puts the turtle down
        t.fillcolor(color) # fills in the color that's been passed into the variable
        t.begin_fill()
        draw_fn() # this simply executes whatever function was passed in.
        t.end_fill()

    # Pumpkin body
    t.setheading(0) #sets the turtle to 0 degrees -> pointing right
    filled_at(x, y, "orange", lambda: t.circle(radius))  # the func lambda is getting passed into draw_fn().
    ''' inside filled_at:
    
       1 filled_at moves the turtle
       2 Starts filling
       3 Calls draw_fn()
       4 Ends filling
       
        When draw_fn() runs, it executes:
            t.circle(radius)
            
        A lambda is just a shortcut way to write a tiny unnamed function that can 
        be passed into another function so it can be 
        executed at the correct time. 
    '''

    # Circle center
    cx = x
    cy = y + radius

    # Stem dimensions
    base = radius / 5
    stem_w = base
    stem_h = radius / 2

    # Put stem on top center. stem_x & stem_y will be passed into the filled_at x, y arguments
    stem_x = cx - stem_w / 2
    stem_y = cy + radius * 0.95  # near top edge

    def stem_path():
        t.setheading(90) # turn the turtle left/north
        t.forward(stem_h)
        t.right(90) # turn the turtle left/west
        t.forward(stem_w)
        t.right(90) # turn the turtle left/south
        t.forward(stem_h)
        t.right(90) # turn the turtle left/east
        t.forward(stem_w)

    filled_at(stem_x, stem_y, "green", stem_path)

    # Eyes (triangles)
    eye_size = radius * 0.25              # takes to eye size down to 1/4 the size of the radius. Allows the eyes to adjust size along with the pumpkin.
    eye_y = cy + radius * 0.05           # slightly above center. Tweak to move eyes up or down.
    eye_dx = radius * 0.28               # horizontal spacing from center

    def eye_path():
        t.setheading(0)
        draw_polygon(t, 3, eye_size) # setting n to 3 draws a triangle

    filled_at(cx - eye_dx - eye_size/2, eye_y, "yellow", eye_path)  # left eye
    filled_at(cx + eye_dx - eye_size/2, eye_y, "yellow", eye_path)  # right eye


    # Mouth (zigzag)
    mouth_width = radius * 0.75         # mouth width will be 3/4 the size of the radius
    mouth_y = cy - radius * 0.55         # below center. Tweak to move mouth up or down
    mouth_x = cx - mouth_width / 2      # Left edge of mouth = center - (width / 2)

    def mouth_path():
        t.setheading(0)
        t.right(60)  # turn turtle right 60 to start the zigzag/keep the mouth straight
        step = mouth_width / 5
        for _ in range(5):
            t.forward(step)
            t.left(120)
            t.forward(step)
            t.right(120)
        t.setheading(0)  # restore turtle orientation to 0 degrees (east)

    filled_at(mouth_x, mouth_y, "yellow", mouth_path)


# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
# t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

draw_pumpkin(t, -150, -250, 100)
draw_pumpkin(t, 0, -250, 80)
draw_pumpkin(t, 150, -250, 100)

# Close the turtle graphics window when clicked
turtle.exitonclick()
