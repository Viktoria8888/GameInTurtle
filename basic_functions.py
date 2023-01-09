import turtle
from parameters import *

def reset_turtle():
    turtle.goto(-turtle.window_width() / 3, -turtle.window_height() / 3)
    turtle.setheading(90)
    if __debug__:
        turtle.dot(10)

def draw_pixel(color="black"):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()

def scale_cords(x, y):
    if x < 0 or x >= ROW_LEN or y < 0 or y >= COL_LEN:
        raise ValueError("Invalid cords")

    return x * PIXEL_SIZE, y * PIXEL_SIZE


if __name__ == "__main__":
    reset_turtle()
    draw_pixel("red")
    turtle.done()