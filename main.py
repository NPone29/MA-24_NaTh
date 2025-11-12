import pygame

grid = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

Player_1 = 0
Player_2 = 1

current_player = Player_1

def get_next_player(current_player):
    if current_player == Player_1:
        return Player_2
    else :
        return Player_1

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    #draw_grid()
    pygame.display.flip