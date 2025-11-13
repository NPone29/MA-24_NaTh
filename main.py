import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (200, 0, 0)

BOARD_WIDTH = 8
BOARD_HEIGHT = 8
TILE_SIZE = 100

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

def pos_to_case(pos):
    return (
        int(pos[0] / TILE_SIZE) % 8,
        int(pos[1] / TILE_SIZE) % 8,
    )

def draw_line(screen, start, end, color=BLACK):
    pygame.draw.line(
        screen,
        color,
        (start[0] * TILE_SIZE, start[1] * TILE_SIZE),
        (end[0] * TILE_SIZE, end[1] * TILE_SIZE),
        5
    )

def draw_grid_lines(screen):
    # vertical lines
    draw_line(screen, (1, 0), (1, 3))
    draw_line(screen, (2, 0), (2, 3))

    # horizontal lines
    draw_line(screen, (0, 1), (3, 1))
    draw_line(screen, (0, 2), (3, 2))

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            case = pos_to_case(pos)
            print(case)

    screen.fill(WHITE)
    #draw_grid()
    pygame.display.flip()