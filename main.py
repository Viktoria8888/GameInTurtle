import turtle
from Board import Board

def turtle_setup():
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0, 0)
    if __debug__:
        turtle.showturtle()


def main():
    turtle_setup()
    board = Board()
    
    board.draw_board_background()
    turtle.done()
    

if __name__ == '__main__':
    main()