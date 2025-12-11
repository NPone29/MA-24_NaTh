import pygame
import core
import json
import sound
pygame.init()
pygame.font.init()

FONT_DEFAULT = pygame.font.SysFont("Arial", 28)
TITLE_FONT = pygame.font.SysFont("Georgia", 38)
UNDER_TITLE_FONT = pygame.font.SysFont("Georgia", 18)

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
BLUE    = (3, 140, 252)
RED     = (255, 0, 0)
GREEN   = (20, 163, 58)
GRAY    = (40, 40, 40)
ORANGE  = (255, 145, 0)

chrono = core.Chronometre()

def _load_scaled(path):
    return pygame.transform.scale(pygame.image.load(path).convert_alpha(), (core.TILE_SIZE, core.TILE_SIZE))

def start_othello():
    core.init_core()
    global screen, background_tile, BLUE_PAWN, BLUE_FR1, BLUE_FR2, BLUE_FR3, RED_PAWN, RED_FR1, RED_FR2, RED_FR3, pause
    screen = pygame.display.set_mode([core.BOARD_WIDTH * core.TILE_SIZE, core.BOARD_HEIGHT * core.TILE_SIZE+50])
    pygame.display.set_caption("MA-24 : Othello game")

    load_background = core.BACKGROUND_IMAGE_PATH
    background_image = pygame.image.load(load_background).convert()
    background_tile = pygame.transform.scale(background_image, (core.TILE_SIZE * 8, core.TILE_SIZE * 8))

    gameIcon = pygame.image.load("Assets/icon.png")
    pygame.display.set_icon(gameIcon)
    BLUE_PAWN     = _load_scaled("Assets/pawns/blue_pawn.png")
    BLUE_FR1      = _load_scaled("Assets/pawns/blue_pawn_fr1.png")
    BLUE_FR2      = _load_scaled("Assets/pawns/blue_pawn_fr2.png")
    BLUE_FR3      = _load_scaled("Assets/pawns/blue_pawn_fr3.png")
    RED_PAWN      = _load_scaled("Assets/pawns/red_pawn.png")
    RED_FR1       = _load_scaled("Assets/pawns/red_pawn_fr1.png")
    RED_FR2       = _load_scaled("Assets/pawns/red_pawn_fr2.png")
    RED_FR3       = _load_scaled("Assets/pawns/red_pawn_fr3.png")
    chrono.reset()
    chrono.start()
    pause = False

start_othello()


pause_btn_image = pygame.image.load("Assets/buttons/pause_buttons.png").convert_alpha()
pause_btn_image = pygame.transform.scale(pause_btn_image,(100,40))
quit_btn_image = pygame.image.load("Assets/buttons/quit_buttons.png").convert_alpha()
quit_btn_image = pygame.transform.scale(quit_btn_image,(100,40))
unpause_btn_image = pygame.image.load("Assets/buttons/unpause_buttons.png").convert_alpha()
unpause_btn_image = pygame.transform.scale(unpause_btn_image,(100,40))




ANIM_INTERVAL_MS = 100
_anim_timestamps = {}  # clé = (x,y) -> dernier tick d'avancement


def pos_to_case(pos,long,larg):
    return (
        int(pos[0] / core.TILE_SIZE) % larg,
        int(pos[1] / core.TILE_SIZE) % long,
    )

def draw_line(screen, start, end):

    json_file_path = "settings.json"
    with open(json_file_path, 'r') as json_file:
        config = json.load(json_file)

    line_larger =int(core.TILE_SIZE/18)
    pygame.draw.line(
        screen,
        config.get("LINE_COLOR", BLACK),
        (start[0] * core.TILE_SIZE, start[1] * core.TILE_SIZE),
        (end[0] * core.TILE_SIZE, end[1] * core.TILE_SIZE),
        line_larger
    )
def draw_text(text, pos, font=FONT_DEFAULT, color=BLACK, center=False):
    surf = font.render(str(text), True, color)
    if center:
        rect = surf.get_rect(center=pos)
    else:
        rect = surf.get_rect(topleft=pos)
    screen.blit(surf, rect)

def draw_sidebar():
    global quit_btn_pos, pause_btn_pos
    rect_x = 0
    rect_y = core.BOARD_HEIGHT*core.TILE_SIZE
    rect_w = core.BOARD_WIDTH*core.TILE_SIZE
    rect_h = 60
    txt_y = rect_y + 9
    pygame.draw.rect(screen, ORANGE, (rect_x, rect_y, rect_w, rect_h), 0)

    #afficher les bouton
    pause_btn_pos = rect_w - 210,rect_y + 5
    quit_btn_pos = rect_w - 105,rect_y + 5
    screen.blit(quit_btn_image,(quit_btn_pos))
    if pause :
        screen.blit(unpause_btn_image,(pause_btn_pos))
    else:
        screen.blit(pause_btn_image,(pause_btn_pos))

    #afficher le score
    score_player1,score_player2 = core.calcul_score()
    draw_text(score_player1,(rect_x+10, txt_y),color = BLUE)
    draw_text(":",(rect_x+40, txt_y),color = BLACK)
    draw_text(score_player2,(rect_x+60, txt_y),color = RED)

    #afficher le temp
    time = chrono.format_temps(chrono.temps_ecoule())
    draw_text(time,(rect_w/4,txt_y))

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
    # coordinates = (col, row)
    col, row = coordinates
    x, y = col, row

    # sécurité indexation
    if y < 0 or y >= len(core.grid) or x < 0 or x >= len(core.grid[y]):
        return

    val = core.grid[y][x]
    # coordinates = (col, row)
    col, row = coordinates
    x, y = col, row

    # sécurité indexation
    if y < 0 or y >= len(core.grid) or x < 0 or x >= len(core.grid[y]):
        return

    val = core.grid[y][x]
    pixel = (x * core.TILE_SIZE, y * core.TILE_SIZE)

    key = (x, y)

    # faire avancer l'animation si la valeur est float (ex: 0.1/0.2/0.3 ou 1.1/1.2/1.3)
    if isinstance(val, float):
        base = int(val)
        frac = round(val - base, 1)  # on attend 0.1, 0.2, 0.3
        now = pygame.time.get_ticks()
        last = _anim_timestamps.get(key)
        if last is None:
            _anim_timestamps[key] = now
        elif now - last >= ANIM_INTERVAL_MS:
            if frac < 0.3:
                # avance une étape d'animation
                core.grid[y][x] = round(val + 0.1, 1)
                _anim_timestamps[key] = now
            else:
                # dernière étape : valeur entière finale
                core.grid[y][x] = base
                _anim_timestamps.pop(key, None)
        # relire la valeur après possible modification
        val = core.grid[y][x]

    # choisir l'image selon la valeur courante
    cur = round(val, 1) if isinstance(val, float) else val

    if cur == 0:
        img = BLUE_PAWN
    elif cur == 1.1:
        img = BLUE_FR1
    elif cur == 1.2:
        img = BLUE_FR2
    elif cur == 1.3:
        img = BLUE_FR3
    elif cur == 1:
        img = RED_PAWN
    elif cur == 0.1:
        img = RED_FR1
    elif cur == 0.2:
        img = RED_FR2
    elif cur == 0.3:
        img = RED_FR3
    else:
        return
    
    screen.blit(img, pixel)

def draw_star(coordinates, player):
    x, y = coordinates
    if player == 0:
        star = pygame.image.load("Assets/stars/blue_star.png")
    else:
        star = pygame.image.load("Assets/stars/red_star.png")
    star = pygame.transform.scale(star, (core.TILE_SIZE, core.TILE_SIZE))
    screen.blit(star, (x * core.TILE_SIZE, y * core.TILE_SIZE))

def draw_hover_star(coordinates):
    x, y = coordinates
    star = pygame.image.load("Assets/stars/star.png")  # image jaune
    star = pygame.transform.scale(star, (core.TILE_SIZE, core.TILE_SIZE))
    screen.blit(star, (x * core.TILE_SIZE, y * core.TILE_SIZE))

def load_player():
    # parcourt par ligne (y) puis colonne (x) — indexation cohérente grid[y][x]
    for y in range(len(core.grid)):
        for x in range(len(core.grid[y])):
            val = core.grid[y][x]
            if val is not None:
                draw_player((x, y), val)
    # parcourt par ligne (y) puis colonne (x) — indexation cohérente grid[y][x]
    for y in range(len(core.grid)):
        for x in range(len(core.grid[y])):
            val = core.grid[y][x]
            if val is not None:
                draw_player((x, y), val)

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
    if not pause :
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
    draw_sidebar()
    if pause:
        rect_h = core.TILE_SIZE * 2
        rect_w = core.TILE_SIZE * core.BOARD_WIDTH
        board_h = core.TILE_SIZE * core.BOARD_HEIGHT
        rect_x = 0
        rect_y = (board_h - rect_h) // 2  # centre vertical
        pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_w, rect_h), 0)
        draw_text("The game is paused.", (rect_x + rect_w // 2, rect_y + rect_h // 2),font=TITLE_FONT, center=True)

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
    
    
    if core.TILE_SIZE * core.BOARD_HEIGHT < 800:
        TITLE_FONT = pygame.font.SysFont("Arial", 22)
        UNDER_TITLE_FONT = pygame.font.SysFont("Georgia", 12)
    else:
        TITLE_FONT = pygame.font.SysFont("Arial", 38)
        UNDER_TITLE_FONT = pygame.font.SysFont("Georgia", 18)
    draw_text(msg, (rect_x + rect_w // 2, rect_y + rect_h // 2),font=TITLE_FONT, color=color_winner, center=True)
    
    chrono.pause()
    time = chrono.format_temps(chrono.temps_ecoule())
    draw_text(time, (rect_x + rect_w // 2, rect_y + rect_h // 2 + core.TILE_SIZE // 3),font=TITLE_FONT, color=BLACK, center=True)

    draw_text("click to continue", (rect_x + rect_w // 2, rect_y + rect_h // 2 + core.TILE_SIZE // 1.5),font=UNDER_TITLE_FONT, color=BLACK, center=True)
    pygame.display.flip()
def btn_ispressed(btn_pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    btn_x,btn_y = btn_pos
    btn_widht = 100
    btn_height = 40
    if (btn_x <= mouse_x <= btn_x + btn_widht and btn_y <= mouse_y <= btn_y + btn_height):
        return True

def pause_game():
    global pause
    pause = not pause
    if pause:
        chrono.pause()
    else:
        chrono.start()

def run_othello():
    start_othello()
    running = True
    clock = pygame.time.Clock()
    while running:
        pos = pygame.mouse.get_pos()
        screen.fill(GREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and core.gamerun == True:
                if pause == False :
                    case = pos_to_case(pos, core.BOARD_HEIGHT, core.BOARD_WIDTH)
                    core.play(case)
                if btn_ispressed(quit_btn_pos):
                    chrono.pause()
                    running=core.leave_game()
                    chrono.start()
                if btn_ispressed(pause_btn_pos):
                    pause_game()
                
            if event.type == pygame.MOUSEBUTTONDOWN and not core.gamerun:
                running = False
        
        core.skip_player()
        if core.gamerun:
            loadscreen()
            place_star(pos)
            pygame.display.flip()
        clock.tick(60)
    pygame.display.quit()
    from start_menu import menu
    menu.afficher_menu()
