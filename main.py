import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (200, 0, 0)

BOARD_WIDTH = 3
BOARD_HEIGHT = 3
TILE_SIZE = 150

screen = pygame.display.set_mode([BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE])
pygame.display.set_caption("MA-24 : Othello game")


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
print(current_player)

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