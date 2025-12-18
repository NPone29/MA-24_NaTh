import json
import sound
from tkinter import *
from tkinter import messagebox
import time
import random

json_file_path = "settings.json"


def create_grid(long,larg):
    grid = []
    for i in range(long):
        row = []
        for j in range(larg):
            row.append(None)
        grid.append(row)

    middlex = int(long/2)
    middley= int(larg/2)

    grid[middlex-1][middley-1] = 0
    grid[middlex-1][middley] = 1
    grid[middlex][middley] = 0
    grid[middlex][middley-1] = 1

    return grid


def init_core():
    global grid, skipped, gamerun, current_player,BACKGROUND_IMAGE_PATH,BOARD_WIDTH,BOARD_HEIGHT,TILE_SIZE,font,folder
    with open(json_file_path, 'r') as json_file:
        config = json.load(json_file)
    font = "Arial"
    folder= "glitch"
    BACKGROUND_IMAGE_PATH = f"Assets/{folder}/backgrounds/background.png"#config.get("BACKGROUND_IMAGE_PATH")
    BOARD_WIDTH = config.get("BOARD_WIDTH")
    BOARD_HEIGHT = config.get("BOARD_HEIGHT")
    TILE_SIZE = config.get("TILE_SIZE")
    grid = create_grid(BOARD_HEIGHT,BOARD_WIDTH)
    skipped =False
    gamerun = True
    current_player = Player_1
    
    

Player_1 = 0
Player_2 = 1


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

    import gfx
    if gfx.bot and current_player == Player_2 and gfx.level == "easy":
        coordinates = choose_move_random(current_player)

    elif gfx.bot and current_player == Player_2 and gfx.level == "hard":
        coordinates = choose_move_greedy(current_player)
    
    x, y = coordinates # Idée de copilot pour décomposer les coordonnées
    
    if grid[y][x] is not None:
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
        print("Invalid move, no pieces captured.")
        return
    grid[y][x] = current_player
    for cx, cy in all_captured:
        grid[cy][cx] = current_player + 0.1

    # Exemple de boucle de flip (ajustez selon votre code réel)
    for (fx, fy) in all_captured:
        grid[fy][fx] = current_player + 0.1  # vous inversez ici le pion
        sound.play_pop()          # jouer le pop pour CE pion

    current_player = get_next_player(current_player)

def check_legal_moves(player):
    legal_moves = []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if grid[y][x] is None:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        captured = rules(grid, player, (x, y), dx, dy)
                        if captured:
                            legal_moves.append((x, y))
                            # dès qu'une direction capture, c'est un coup légal -> passer à la case suivante
                            dx = dy = None
                            break
                    if dx is None:
                        break
    return legal_moves


def skip_player():
    global skipped, current_player

    legal_moves = check_legal_moves(current_player)

    if not legal_moves :
        if skipped == True :
            gameover()
        else :
            current_player = get_next_player(current_player)
            print(current_player," skipped")
            skipped = True
    else :
        skipped = False
def calcul_score():
    score_player1 = 0
    score_player2 = 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                score_player1 +=1
            if grid[x][y] == 1:
                score_player2 +=1
    return score_player1,score_player2



def gameover() :
    import gfx
    global gamerun
    if gamerun :
        sound.stop_game_music()
        sound.play_winner()
    gamerun = False
    score_player1,score_player2 = calcul_score()


    if score_player2 > score_player1 :
        winnerplayer = "Player_2"

    elif score_player1 > score_player2 :
        winnerplayer = "Player_1"
    else :
        winnerplayer = None

    gfx.loadscreen()

    gfx.draw_gameover(winnerplayer,score_player1,score_player2)

def leave_game():
    
    if messagebox.askyesno("Leave Game", "Do you want to leave the game?"):
        return False
    else:
        return True

class Chronometre: #Le web m'a aidé pour cette classe.
    def __init__(self):
        self.start_time = None   # Heure de départ
        self.elapsed = 0.0       # Temps écoulé cumulé
        self.running = False     # État du chronomètre

    def start(self):
        #Démarre ou reprend le chronomètre.
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True

    def pause(self):
        #Met en pause le chronomètre.
        if self.running:
            self.elapsed += time.perf_counter() - self.start_time
            self.running = False

    def reset(self):
        #Réinitialise le chronomètre.
        self.start_time = None
        self.elapsed = 0.0
        self.running = False

    def temps_ecoule(self):
        #Retourne le temps écoulé en secondes.
        if self.running:
            return self.elapsed + (time.perf_counter() - self.start_time)
        return self.elapsed

    @staticmethod
    def format_temps(secondes):
        #Formate le temps en HH:MM:SS
        heures = int(secondes // 3600)
        minutes = int((secondes % 3600) // 60)
        secs = int(secondes % 60)
        return f"{heures:02}:{minutes:02}:{secs:02}"

def choose_move_random(player):
    moves = check_legal_moves(player)
    return random.choice(moves) if moves else None

def choose_move_greedy(player): # J'ai demandé de l'aide à copilot pour cette fonction. Parce que je ne savais pas comment faire. "Peux tu m'aider à faire une fonction qui choisit le meilleur coup possible en fonction du nombre de pions capturés ?"
    best = None
    best_count = -1
    for move in check_legal_moves(player):
        total = 0
        x, y = move
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                caps = rules(grid, player, (x, y), dx, dy)
                total += len(caps)
        if total > best_count:
            best_count = total
            best = move
    return best