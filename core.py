import gfx

grid = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, 0, 1, None, None, None],
    [None, None, None, 1, 0, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
TILE_SIZE = 100

def play(coordinates):
    global grid, current_player

    x, y = coordinates # Idée de copilot pour décomposer les coordonnées
    if grid[y][x] == None:
        grid[y][x] = current_player
        gfx.draw_player(coordinates, current_player)
    else:
        color =grid[y][x]
        change_color(color,coordinates)
        return

    current_player = get_next_player(current_player)

def change_color(color,pos):
    x,y = pos
    if color == 0:
        grid[y][x] = 1
    elif color ==1:
        grid[y][x] = 0
    else :
        print("error, can't replace color at ",y,x)

Player_1 = 0
Player_2 = 1

current_player = Player_1

def get_next_player(current_player):
    if current_player == Player_1:
        return Player_2
    else :
        return Player_1
    