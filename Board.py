from parameters import *
from basic_functions import *

class Board:
    def __init__(self, turtle) -> None:
        pass

    def draw_board_background(self):
        reset_turtle()
        turtle.fillcolor("grey")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(ROW_LEN * PIXEL_SIZE)
            turtle.right(90)
            turtle.forward(COL_LEN * PIXEL_SIZE)
            turtle.right(90)
        turtle.end_fill()


if __name__ == "__main__":
    board = Board()
    board.draw_board_background()
    turtle.done()
    
        
    