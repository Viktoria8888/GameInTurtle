import turtle
from parameters import *

def reset_turtle():
    turtle.goto(LEFT_SWITCH, RIGHT_SWITCH)
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

def move_turtle(x, y):
    x, y = scale_cords(x, y)
    turtle.goto(x + LEFT_SWITCH, y + RIGHT_SWITCH)
    
def scale_cords(x, y):
    if x < 0 or x >= ROW_LEN or y < 0 or y >= COL_LEN:
        raise ValueError("Invalid cords", x, y)

    return x * PIXEL_SIZE, y * PIXEL_SIZE

def is_collision_comet_airplane(comet, airplane):
    for x, y in airplane.body:
        if comet.x == x and comet.y == y:
            return True
    return False


if __name__ == "__main__":
    reset_turtle()
    draw_pixel("red")
    turtle.done()