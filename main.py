import turtle
from Board import Board
from Airplane import Airplane

def turtle_setup():
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0, 0)
    if __debug__:
        turtle.showturtle()
        turtle.speed(1)
        turtle.tracer(1, 0)


def main():
    turtle_setup()
    board = Board(turtle)
    airplane = Airplane(turtle)
    
    board.draw_board_background()
    airplane.draw_airplane()
    turtle.done()
    

if __name__ == '__main__':
    main()