import turtle
from Board import Board
from Airplane import Airplane
from Comet import Comet
import time
from pynput import keyboard
from basic_functions import *

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

    def key_pressed(key):
        if key == keyboard.Key.right:
            airplane.move_right()
        if key == keyboard.Key.left:
            airplane.move_left()

    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    
    while True:
        for faze in range(3):
            turtle.clear()
            board.draw_board_background()
            if faze == 0:
                for comet in comets:
                    comet.update_comet()
            for comet in comets:
                comet.draw_comet()
                if is_collision_comet_airplane(comet, airplane):
                    print("Game Over")
                    exit()
            
            airplane.draw_airplane()
            
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