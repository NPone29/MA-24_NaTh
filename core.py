import gfx
import pygame
import tkinter as tk
from tkinter import messagebox

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
TILE_SIZE = 100

def create_grid(long,larg):
    grid = []
    for i in range(long):
        row = []
        for j in range(larg):
            row.append(None)
        grid.append(row)

    middlex = int(long/2)
    middley= int(larg/2)

    grid[middley-1][middlex-1] = 0
    grid[middley][middlex-1] = 1
    grid[middley][middlex] = 0
    grid[middley-1][middlex] = 1

    return grid



grid = create_grid(BOARD_HEIGHT,BOARD_WIDTH)
print(grid)

Player_1 = 0
Player_2 = 1

current_player = Player_1

def get_next_player(current_player):
    if current_player == Player_1:
        return Player_2
    else :
        return Player_1


def is_on_board(x, y):
    return 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT #Idée de copilot, parce que je n'avais pas d'idée de comment faire. Comment faire pour faire une fonction qui regarde si le pion est bien dans le

def rules(grid, player, coordinates, dx, dy):
    captured = []
    x, y = coordinates
    cx, cy = x + dx, y + dy

    while is_on_board(cx, cy) and grid[cy][cx] == get_next_player(player):
        captured.append((cx, cy))
        cx += dx
        cy += dy

    if is_on_board(cx, cy) and grid[cy][cx] == player and captured:
        return captured
    return []



def play(coordinates):
    global grid, current_player

    x, y = coordinates # Idée de copilot pour décomposer les coordonnées
    
    if grid[y][x] is not None:
        messagebox.showerror("Invalid Move", "Invalid move, cell already occupied.")
        print("Invalid move, cell already occupied.")
        return
    all_captured = []
    for dx in [-1, 0, 1]: # Idée de copilot pour faire cette boucle imbriquée. Parce que j'avais des problèmes alors j'ai lui ai demandé pour débuger. "Y a t'il des problèmes dans ma fonction play ?"
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            captured = rules(grid, current_player, (x, y), dx, dy)
            all_captured.extend(captured)
    if not all_captured:
        messagebox.showerror("Invalid Move", "Invalid move, no pieces captured.")
        print("Invalid move, no pieces captured.")
        return
    grid[y][x] = current_player
    for cx, cy in all_captured:
        grid[cy][cx] = current_player

    current_player = get_next_player(current_player)

def change_color(color,pos):
    x,y = pos
    if color == 0:
        grid[y][x] = 1
    elif color ==1:
        grid[y][x] = 0
    else :
        print("error, can't replace color at ",y,x)


