from parameters import *
from basic_functions import *

class Board:
    def __init__(self, turtle) -> None:
        pass

    def draw_board_background(self):
        for y in range(COL_LEN):
            for x in range(ROW_LEN):
                move_turtle(x, y)
                draw_pixel("grey")

if __name__ == "__main__":
    board = Board()
    board.draw_board_background()
    turtle.done()
    
        
    