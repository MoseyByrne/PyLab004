#!/usr/bin/env python3
"""
This is a fun little group of functions I made to entertain you. If you found this, congratulations! You're curious!
If you have questions about it, let me know!

Cheers,
Trevor
"""
import turtle
import math
import random

def draw_polyline(t, n, length, angle):  # This is really generalized and flexible now.
    """Draws line segments with the given length and angle between them.

    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """
    for i in range(n):
        t.forward(length)
        t.left(angle)

def draw_polygon(t, n, length):
    angle = 360.0 / n
    # Now this is more generalized as it uses polyline, but still fixes the length and angle for regular polygons.
    draw_polyline(t, n, length, angle)

def draw_arc(t, radius, angle):  # Similar to circle, but can do fractional circles.
    arc_length = 2 * math.pi * radius * angle / 360  # Here we calculate how much of the arc of a circle to draw.
    n = 30  # We fix the segments to 30 still, but this is 30 segments per arc, so smaller arcs will appear smoother.
    length = arc_length / n
    step_angle = angle / n  # Since we are covering a fraction of the arc of a circle, we need smaller angles too.
    draw_polyline(t, n, length, step_angle)  # And now we approximate the arc with polyline.

def draw_circle(t, radius):  # Generalized circle function based off arc based off polyline
    draw_arc(t, radius, 360)

def draw_square(t, length):
    draw_polygon(t, 4, length)

def draw_parallelogram(t, base, leg, interior_angle):
    """Draws a quadrilateral with parallel sides, a more generalized form of rhombus and rectangle.

    :param base: base of quadrilateral
    :param leg: side of quadrilateral
    :param interior_angle: first interior angle of quadrilateral
    :return: None
    """
    for i in range(2):  # Just like rhombus and rectangle before, there are 2 symmetric parts.
        for side, angle in ((base, interior_angle), (leg, 180 - interior_angle)):
            # Draw base and turn, then draw leg and turn complementary
            draw_polyline(t, 1, side, angle)

def draw_rhombus(t, base, interior_angle):
    """Rhombus drawn with generalized parallelogram / quadrilateral function

    :param base: side of rhombus
    :param interior_angle: First interior angle of rhombus
    :return: None
    """
    draw_parallelogram(t, base, base, interior_angle)

def draw_rectangle(t, b, h):
    """Rectangle drawn with generalized parallelogram / quadrilateral function

    :param b: base of rectangle
    :param h: height of rectangle
    :return: None
    """
    draw_parallelogram(t, base=b, leg=h, interior_angle=90)

def shape_factory(t, shape_type, base, leg=None, angle=90):
    leg = base if leg is None else leg
    match shape_type:
        case "circle":
            return lambda: draw_circle(t, base)
        case "polygon":
            return lambda n: draw_polygon(t, base, n)
        case "parallelogram":
            return lambda: draw_parallelogram(t, base, leg, angle)
        case "rectangle":
            return lambda: draw_rectangle(t, base, leg)
        case "rhombus":
            return lambda: draw_rhombus(t, base, angle)
        case "square":
            return lambda: draw_square(t, base)

def draw(t, my_colors):
    t.speed( 10 )  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
    for shape in ['square', 'circle', 'rhombus', 'rectangle', 'parallelogram', 'polygon']:
        t.color( my_colors[random.randint( 0, 5 )] )
        size = random.randint( 20, 80 )
        angle = 90 if shape in ['square', 'circle', 'rectangle'] else random.randint( 20, 80 )
        leg = size if shape in ['square', 'circle', 'rhombus', 'rectangle'] else random.randint( 20, 80 )
        shape_func_obj = shape_factory(t, shape, size, leg, angle )
        shape_func_obj() if shape in ['square', 'circle', 'rhombus', 'rectangle', 'parallelogram'] \
            else shape_func_obj(random.randint( 3, 12 ) )
        random_jump(t)

def random_jump(t, min_jump=20, max_jump=120, min_turn=10, max_turn=359):
    t.penup()
    t.forward( random.randint(min_jump, max_jump) )
    t.left(random.randint(min_turn, max_turn))
    t.pendown()

if __name__ == '__main__':
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("black")
    # Set the width and height of the screen
    screen.setup(width=500, height=500)
    # Create a new turtle object, equivalent to Jupyter's make_turtle
    my_turtle = turtle.Turtle()

    # Set the turtle's shape and color
    my_turtle.shape("circle")  # Other options: arrow, classic, square, triangle, and turtle
    # Draw with a turtle.
    draw(my_turtle, ['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

    # Close the turtle graphics window when clicked
    turtle.exitonclick()