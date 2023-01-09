from turtle import *
from parameters import *
from basic_functions import *
window = Screen()
window.setup()

class Airplane:
    def __init__(self, turtle):
        self.body = [[0,0], [1, 0], [2, 0],
                     [0, 1], [1, 1], [2, 1],
                     [0, 2], [1, 2], [2, 2]]
          
    def move_right(self):
        most_right_x = self.body[2][0]
        if most_right_x >= ROW_LEN - 1: return

        for coordinate in self.body:
            coordinate[0] += 1

    def move_left(self):
        most_left_x = self.body[0][0]
        if most_left_x <= 0: return

        for coordinate in self.body:
            coordinate[0] -= 1

    def draw_airplane(self):
        for x, y in self.body:
            move_turtle(x, y)
            draw_pixel("red")

    
    def if_out(self):
        if self.x < 0 or self.x >= ROW_LEN:
            return True
        return False

# key bindings
if __name__ == "__main__":
    airplane_object = Airplane()
    airplane_object.draw_airplane()
    window.onkeypress(airplane_object.left_click(), "Left")
    window.onkeypress(airplane_object.right_click(), "Right")
    window.listen()

    mainloop()