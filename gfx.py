import pygame
import random
import core

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (200, 0, 0)



screen = pygame.display.set_mode([core.BOARD_WIDTH * core.TILE_SIZE, core.BOARD_HEIGHT * core.TILE_SIZE])
pygame.display.set_caption("MA-24 : Othello game")

background = pygame.image.load("Assets/background.png")  # on charge l'arrière plan (code donné par copilot)
background = pygame.transform.scale(background, (800, 800))

gameIcon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(gameIcon)



def     pos_to_case(pos):
    return (
        int(pos[0] / core.TILE_SIZE) % 8,
        int(pos[1] / core.TILE_SIZE) % 8,
    )

def draw_line(screen, start, end, color=BLACK):
    pygame.draw.line(
        screen,
        color,
        (start[0] * core.TILE_SIZE, start[1] * core.TILE_SIZE),
        (end[0] * core.TILE_SIZE, end[1] * core.TILE_SIZE),
        7
    )

def draw_grid_lines(screen):
    # vertical lines
    draw_line(screen, (1, 0), (1, 8))
    draw_line(screen, (2, 0), (2, 8))
    draw_line(screen, (3, 0), (3, 8))
    draw_line(screen, (4, 0), (4, 8))
    draw_line(screen, (5, 0), (5, 8))
    draw_line(screen, (6, 0), (6, 8))
    draw_line(screen, (7, 0), (7, 8))

    # horizontal lines
    draw_line(screen, (0, 1), (8, 1))
    draw_line(screen, (0, 2), (8, 2))
    draw_line(screen, (0, 3), (8, 3))
    draw_line(screen, (0, 4), (8, 4))
    draw_line(screen, (0, 5), (8, 5))
    draw_line(screen, (0, 6), (8, 6))
    draw_line(screen, (0, 7), (8, 7))

def draw_player(coordinates, player):
    blue_pawn = pygame.image.load("Assets/blue_pawn.png")
    red_pawn = pygame.image.load("Assets/red_pawn.png")

    x, y = coordinates # Idée de copilot pour décomposer les coordonnées
    pixel = (x * core.TILE_SIZE, y * core.TILE_SIZE)

    if player == 0:
        bleu_pawn = pygame.transform.scale(blue_pawn, (core.TILE_SIZE, core.TILE_SIZE))

        rect = bleu_pawn.get_rect(topleft=pixel)
        screen.blit(bleu_pawn, rect)
    elif player == 1:

        red_pawn = pygame.transform.scale(red_pawn, (core.TILE_SIZE, core.TILE_SIZE))

        rect = red_pawn.get_rect(topleft=pixel)
        screen.blit(red_pawn, rect)

def load_player():
    for x in range(len(core.grid)):
        for y in range(len(core.grid[x])):
            if core.grid[x][y] == 0:
                draw_player((y, x), 0)
            elif core.grid[x][y] == 1:
                draw_player((y, x), 1)




def run_othello():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                case = pos_to_case(pos)
                print(case)
                core.play(case)
        

        screen.blit(background, (0, 0))  # Affiche l’image à la position (0, 0) (code généré par copilot)

        load_player()
        draw_grid_lines(screen)# draw_grid()
        pygame.display.flip()  # Met à jour l’écran
