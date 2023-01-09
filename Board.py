from parameters import *
from basic_functions import *
import turtle

class Board:
    def __init__(self) -> None:
        pass

    def draw_board_background(self):
        print("Drawing board background")
        print(COL_LEN, ROW_LEN)
        for y in range(COL_LEN):
            for x in range(ROW_LEN):
                print(x, y)
                move_turtle(x, y)
                draw_pixel("grey")

if __name__ == "__main__":
    board = Board()
    board.draw_board_background()
    turtle.done()
    
        
    