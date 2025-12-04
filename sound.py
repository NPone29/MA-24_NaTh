import pygame
import pygame
pygame.mixer.init()
try:
    POP_SOUND = pygame.mixer.Sound("Assets/sounds/pop.mp3")
except Exception:
    POP_SOUND = None

try:
    MENU_SOUND = pygame.mixer.Sound("Assets/sounds/menu.mp3")
except Exception:
    MENU_SOUND = None

try:
    START_SOUND = pygame.mixer.Sound("Assets/sounds/start.mp3")
except Exception:
    START_SOUND = None

def play_pop():
    if POP_SOUND:
        POP_SOUND.play()

def play_menu(loop):
    if MENU_SOUND:
        if loop == True:
            MENU_SOUND.play(loops=-1)
        else:
            MENU_SOUND.play()

def stop_menu():
    if MENU_SOUND:
        MENU_SOUND.stop()

def play_start():
    if START_SOUND:
        START_SOUND.play()
        print("play start")