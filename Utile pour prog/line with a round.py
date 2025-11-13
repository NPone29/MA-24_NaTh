import pygame

pygame.init()

BOARD_WIDTH = 4
BOARD_HEIGHT = 1
TILE_SIZE = 100

screen = pygame.display.set_mode([BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE])

pygame.display.set_caption("MA-24 : Bases de pygame")

screen.fill((255, 255, 255))

def draw_line(screen, start, end, color=(0, 0, 0)):
    pygame.draw.line(
        screen,
        color,
        (start[0] * TILE_SIZE, start[1] * TILE_SIZE),
        (end[0] * TILE_SIZE, end[1] * TILE_SIZE),
        5
    )
draw_line(screen, (1, 0), (1, 1))
draw_line(screen, (2, 0), (2, 1))
draw_line(screen, (3, 0), (3, 1))
draw_line(screen, (0, 0), (4, 0))
draw_line(screen, (0, 1), (4, 1))

pygame.draw.circle(screen,(0, 0, 0), (150, 50),45)
pygame.display.flip()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()
        pygame.display.update()

pygame.quit()



