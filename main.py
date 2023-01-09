import turtle
from Board import Board
from Airplane import Airplane
from Comet import Comet
import time

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
    comets = [Comet(turtle) for _ in range(15)]

    board.draw_board_background()
    airplane.draw_airplane()
    
    while True:
        turtle.clear()
        board.draw_board_background()
        for comet in comets:
            comet.update_comet()
        for comet in comets:
            comet.draw_comet()
        turtle.update()
        time.sleep(0.01)
        
        

    turtle.done()
    

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        turtle.done()
        exit()