from turtle import *
from parameters import *
from basic_functions import *
window = Screen()
window.setup()

class Airplane:
    def __init__(self, turtle):
        self.x = 0
          
    def right_click(self):
        self.x = self.x + 1
    def left_click(self):
        self.x = self.x - 1

    def draw_airplane(self):
        move_turtle(self.x, 1)
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