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

snake_head = Tile(5, 5)
food = Tile(20, 20)
snake_body = []
velocity_x= 0
velocity_y= 0
game_over = False

def change_direction(e):
    global velocity_x, velocity_y
    if e.keysym =="Up" and velocity_y!= 1:
        velocity_x = 0
        velocity_y =  -1
    elif e.keysym == "Down" and velocity_y != -1:
        velocity_x= 0
        velocity_y= 1
    elif e.keysym =="Left" and velocity_x != 1:
        velocity_x= -1
        velocity_y= 0
    elif e.keysym == "Right" and velocity_x!= -1:
        velocity_x = 1
        velocity_y = 0

def move_snake():
    global snake_head, snake_body, food, game_over

    if (game_over):
        return

    if (snake_head.x < 0 or snake_head.x >= COLS or snake_head.y < 0 or snake_head.y >= ROWS):
        game_over = True
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="GAmeover", fill= "white", font= ("Arial",30))
        return

    for i in snake_body:
        if snake_head.x == i.x and snake_head.y == i.y:
            game_over= True
            canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="GAmeover", fill= "white", font= ("Arial",30))
            return
    
    if snake_head.x == food.x and snake_head.y == food.y:
        snake_body.append(Tile(food.x,food.y))
        food.x = random.randint(0, COLS-1)
        food.y= random.randint(0, ROWS-1)

    for i in range(len(snake_body) -1,-1,-1):
        if i== 0:
            snake_body[i].x =snake_head.x
            snake_body[i].y = snake_head.y
        else:
            snake_body[i].x= snake_body[i-1].x
            snake_body[i].y= snake_body[i-1].y

    snake_head.x += velocity_x
    snake_head.y += velocity_y


def draw():
    global snake_head, food

    move_snake()
    canvas.delete("all")
    canvas.create_rectangle(food.x * TILE_SIZE, food.y * TILE_SIZE, (food.x+1) * TILE_SIZE, (food.y +1)* TILE_SIZE, fill = "red")
    canvas.create_rectangle(snake_head.x * TILE_SIZE, snake_head.y * TILE_SIZE, (snake_head.x +1) * TILE_SIZE, (snake_head.y +1)* TILE_SIZE,fill="blue")
    
    for i in snake_body:
        canvas.create_rectangle(i.x*TILE_SIZE, i.y*TILE_SIZE, (i.x+1)*TILE_SIZE, (i.y+1)*TILE_SIZE, fill="blue")

    if game_over:
         canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 30))
         return 

    window.after(200, draw)
draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()