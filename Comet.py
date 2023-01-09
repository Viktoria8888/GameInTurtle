import random
from parameters import *
from basic_functions import *

class Comet:
    def __init__(self, turtle):
        self.x = random.randint(0, ROW_LEN - 1)
        self.y = random.randint(0, COL_LEN - 1)
        self.direction = random.choice([(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)])

    def draw_comet(self):
        move_turtle(self.x, self.y)
        draw_pixel('brown')
    
    def erase_comet(self):
        move_turtle(self.x, self.y)
        draw_pixel('gray')

    def update_comet(self):
        self.erase_comet()

        self.x += self.direction[0]
        self.y += self.direction[1]

        if self.x < 0:
            self.x = ROW_LEN - 1
        if self.x >= ROW_LEN:
            self.x = 0
        if self.y < 0:
            self.y = COL_LEN - 1
        if self.y >= COL_LEN:
            self.y = 0

        print(self.x, self.y)

    
        