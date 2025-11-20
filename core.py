import gfx

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

    


    

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
TILE_SIZE = 100

grid = create_grid(BOARD_HEIGHT,BOARD_WIDTH)
print(grid)
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

