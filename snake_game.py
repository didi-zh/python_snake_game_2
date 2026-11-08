import tkinter as tk
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE*COLS
WINDOW_HEIGHT = TILE_SIZE*ROWS

class Tile:
    def __init__(self, x, y):
    self.x = x
    self.y = y 

window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tk.Canvas(window, bg= "black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()
window.update()

window.mainloop()