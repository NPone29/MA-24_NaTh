from pygame import mixer
import json

def init_sound():
    global sound_on
    json_file_path = "settings.json"
    with open(json_file_path, 'r') as json_file:
        config = json.load(json_file)
        
    sound_on = config.get("sound")
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

init_sound()

def play_pop():
    if POP_SOUND:
        POP_SOUND.play()
        POP_SOUND.set_volume(sound_on)

def play_menu(loop):
    if MENU_SOUND:
        if loop == True:
            MENU_SOUND.play(loops=-1)
        else:
            MENU_SOUND.play()
    MENU_SOUND.set_volume(sound_on)

def stop_menu():
    if MENU_SOUND:
        MENU_SOUND.stop()

def play_start():
    if START_SOUND:
        START_SOUND.play()
        START_SOUND.set_volume(sound_on)