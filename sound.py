from pygame import mixer
import json

def init_sound():
    global volume, music_on, sound_on
    json_file_path = "settings.json"
    with open(json_file_path, 'r') as json_file:
        config = json.load(json_file)
        
    volume = config.get("volume", 0.5)
    music_on = config.get("music", 1)
    sound_on = config.get("sound", 1)
mixer.init()
try:
    POP_SOUND = mixer.Sound("Assets/sounds/pop.mp3")
except Exception:
    POP_SOUND = None

try:
    MENU_SOUND = mixer.Sound("Assets/sounds/menu.mp3")
except Exception:
    MENU_SOUND = None

try:
    START_SOUND = mixer.Sound("Assets/sounds/start.mp3")
except Exception:
    START_SOUND = None

try:
    GAME_MUSIC = mixer.Sound("Assets/sounds/game_music.mp3")
except Exception:
    GAME_MUSIC = None

try:
    WINNER_MUSIC = mixer.Sound("Assets/sounds/winner.mp3")
except Exception:
    WINNER_MUSIC = None

init_sound()

def play_pop():
    if POP_SOUND and sound_on > 0:
        POP_SOUND.play()
        POP_SOUND.set_volume(volume)

def play_menu(loop=True):
    if MENU_SOUND and music_on > 0:
        MENU_SOUND.set_volume(volume)
        if loop:
            MENU_SOUND.play(loops=-1)
        else:
            MENU_SOUND.play()

def stop_menu():
    if MENU_SOUND:
        MENU_SOUND.stop()

def play_start():
    if START_SOUND and sound_on > 0:
        START_SOUND.play()
        START_SOUND.set_volume(volume)

def play_game_music(loop=True):
    if GAME_MUSIC and music_on > 0:
        GAME_MUSIC.set_volume(volume)
        if loop:
            GAME_MUSIC.play(loops=-1)
        else:
            GAME_MUSIC.play()


def stop_game_music():
    if GAME_MUSIC:
        GAME_MUSIC.stop()

def play_winner(loop=True):
    if WINNER_MUSIC and sound_on > 0:
        WINNER_MUSIC.set_volume(volume)
        if loop:
            WINNER_MUSIC.play(loops=-1)
        else:
            WINNER_MUSIC.play()
def stop_winner_music():
    if WINNER_MUSIC:
        WINNER_MUSIC.stop()