import pygame
import core

pygame.init()
pygame.font.init()

FONT_DEFAULT = pygame.font.SysFont("Arial", 28)
TITLE_FONT = pygame.font.SysFont("Georgia", 38)
UNDER_TITLE_FONT = pygame.font.SysFont("Georgia", 18)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (200, 0, 0)
GREEN =(20, 163, 58)



screen = pygame.display.set_mode([core.BOARD_WIDTH * core.TILE_SIZE, core.BOARD_HEIGHT * core.TILE_SIZE])
pygame.display.set_caption("MA-24 : Othello game")

background_image = pygame.image.load("Assets/flowery_background.png").convert()
background_tile = pygame.transform.scale(background_image, (core.TILE_SIZE * 8, core.TILE_SIZE * 8))

gameIcon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(gameIcon)



def pos_to_case(pos,long,larg):
    return (
        int(pos[0] / core.TILE_SIZE) % larg,
        int(pos[1] / core.TILE_SIZE) % long,
    )

def draw_line(screen, start, end, color=BLACK):
    line_larger =int(core.TILE_SIZE/14)
    pygame.draw.line(
        screen,
        color,
        (start[0] * core.TILE_SIZE, start[1] * core.TILE_SIZE),
        (end[0] * core.TILE_SIZE, end[1] * core.TILE_SIZE),
        line_larger
    )

def draw_grid_lines(screen, long,larg):
    # vertical lines
    if long>larg:
        max = long
    else:
        max = larg

    for i in range(larg-1):
        draw_line(screen, (i+1, 0), (i+1,max))

    # horizontal lines
    for i in range(larg-1):
        draw_line(screen, (0, i+1), (max,i+1))

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
        
def draw_star(coordinates, player):
    x, y = coordinates
    if player == 0:
        star = pygame.image.load("Assets/blue_star.png")
    else:
        star = pygame.image.load("Assets/red_star.png")
    star = pygame.transform.scale(star, (core.TILE_SIZE, core.TILE_SIZE))
    screen.blit(star, (x * core.TILE_SIZE, y * core.TILE_SIZE))

def draw_hover_star(coordinates):
    x, y = coordinates
    star = pygame.image.load("Assets/star.png")  # image jaune
    star = pygame.transform.scale(star, (core.TILE_SIZE, core.TILE_SIZE))
    screen.blit(star, (x * core.TILE_SIZE, y * core.TILE_SIZE))

def load_player():
    for x in range(len(core.grid)):
        for y in range(len(core.grid[x])):
            if core.grid[x][y] == 0:
                draw_player((y, x), 0)
            elif core.grid[x][y] == 1:
                draw_player((y, x), 1)

def check_legal_moves(player):
    legal_moves = []
    for x in range(core.BOARD_WIDTH):
        for y in range(core.BOARD_HEIGHT):
            if core.grid[y][x] is None:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        captured = core.rules(core.grid, player, (x, y), dx, dy)
                        if captured:
                            legal_moves.append((x, y))
                            # dès qu'une direction capture, c'est un coup légal -> passer à la case suivante
                            dx = dy = None
                            break
                    if dx is None:
                        break
    return legal_moves
def repeat_bg() :
        board_px_w = core.BOARD_WIDTH * core.TILE_SIZE
        board_px_h = core.BOARD_HEIGHT * core.TILE_SIZE
        tile_w = background_tile.get_width()
        tile_h = background_tile.get_height()
        for bx in range(0, board_px_w, tile_w):
            for by in range(0, board_px_h, tile_h):
                screen.blit(background_tile, (bx, by))

def place_star(pos):
    legal_moves = check_legal_moves(core.current_player)

    mouse_case = pos_to_case(pos, core.BOARD_HEIGHT, core.BOARD_WIDTH)

    for move in legal_moves:
        if move == mouse_case:
            draw_hover_star(move)
        else:
            draw_star(move, core.current_player)

def loadscreen():

    repeat_bg()# Répéter le bloc 8x8 (background_tile) pour couvrir dynamiquement la taille du plateau (code de copilot UNIQUEMENT pour répéter l'arrière plan)
    draw_grid_lines(screen,core.BOARD_HEIGHT,core.BOARD_WIDTH)# draw_grid()

    load_player()

def draw_text(text, pos, font=FONT_DEFAULT, color=BLACK, center=False):
    """Dessine du texte sur l'écran. pos = (x,y). Si center=True, pos est le centre."""
    surf = font.render(str(text), True, color)
    if center:
        rect = surf.get_rect(center=pos)
    else:
        rect = surf.get_rect(topleft=pos)
    screen.blit(surf, rect)

def draw_gameover(winner,score_1, score_2) :
    # hauteur = 2 cases, largeur = largeur du plateau, centré verticalement
    rect_h = core.TILE_SIZE * 2
    rect_w = core.TILE_SIZE * core.BOARD_WIDTH
    board_h = core.TILE_SIZE * core.BOARD_HEIGHT
    rect_x = 0
    rect_y = (board_h - rect_h) // 2  # centre vertical
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_w, rect_h), 0)

    if winner == "Player_1" :
        msg = f"End of the game, the Blues won ! — {score_1} to {score_2}"
        color_winner = BLUE
    elif winner == "Player_2":
        msg = f"End of the game, the Reds won ! — {score_2} to {score_1}"
        color_winner = RED
    elif winner == None :
        msg = f"Fin de la partie, égalité ! — {score_2} to {score_1}"
        color_winner = BLACK
    
        
    draw_text(msg, (rect_x + rect_w // 2, rect_y + rect_h // 2),font=TITLE_FONT, color=color_winner, center=True)
    draw_text("click to continue", (rect_x + rect_w // 2, rect_y + rect_h // 2 + core.TILE_SIZE // 3),font=UNDER_TITLE_FONT, color=BLACK, center=True)
    pygame.display.flip()


def run_othello():
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        screen.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and core.gamerun == True:
                case = pos_to_case(pos, core.BOARD_HEIGHT, core.BOARD_WIDTH)
                print(case)
                core.play(case)
            if event.type == pygame.MOUSEBUTTONDOWN and core.gamerun == False:
                pygame.quit()
                from start_menu import menu
                menu.afficher_menu()
                return
        core.skip_player()

        if core.gamerun == True:
            loadscreen()
            place_star(pos)
            pygame.display.flip()  # Met à jour l’écran
        