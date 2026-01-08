import json
import os
from utils import resource_path

# Default globals
sound_on = 1
volume = 0.5
folder = json.load(open("settings.json")).get("folder","default")
mixer_available = False

POP_SOUND = None
MENU_SOUND = None
START_SOUND = None
GAME_MUSIC = None
WINNER_MUSIC = None


def _ensure_mixer():
    """Try to initialize pygame.mixer safely and return (mixer_module or None)."""
    global mixer_available
    try:
        import pygame
        if getattr(pygame, "mixer", None) is None:
            mixer_available = False
            return None
        if not pygame.mixer.get_init():
            try:
                pygame.mixer.init()
            except Exception as e:
                # failed to init mixer
                print("pygame.mixer.init failed:", e)
                mixer_available = False
                return None
        mixer_available = True
        return pygame.mixer
    except Exception as e:
        mixer_available = False
        print("pygame not available for mixer:", e)
        return None


def init_sound():
    """Read settings.json and (re)initialize mixer and Sound objects.
    Safe to call multiple times.
    """
    global sound_on, volume, folder
    global POP_SOUND, MENU_SOUND, START_SOUND, GAME_MUSIC, WINNER_MUSIC

    # read settings
    try:
        with open(resource_path("settings.json"), "r", encoding="utf-8") as f:
            cfg = json.load(f)
            sound_on = cfg.get("sound", 1)
            volume = cfg.get("volume", 0.5)
    except Exception as e:
        print("Could not read settings.json in init_sound:", e)

    # ensure mixer
    mixer = _ensure_mixer()

    # reset sound objects
    POP_SOUND = MENU_SOUND = START_SOUND = GAME_MUSIC = WINNER_MUSIC = None

    if mixer is None:
        return

    # load sounds, tolerate missing files
    def _load(path):
        try:
            s = mixer.Sound(resource_path(path))
            return s
        except Exception as e:
            print(f"Failed to load sound {path}:", e)
            return None

    POP_SOUND = _load(f"Assets/{folder}/sounds/pop.mp3")
    if POP_SOUND:
        try:
            POP_SOUND.set_volume(volume)
        except Exception as e:
            print("Failed to set POP_SOUND volume:", e)

    MENU_SOUND = _load(f"Assets/{folder}/sounds/menu.mp3")
    if MENU_SOUND:
        try:
            MENU_SOUND.set_volume(volume)
        except Exception as e:
            print("Failed to set MENU_SOUND volume:", e)

    START_SOUND = _load(f"Assets/{folder}/sounds/start.mp3")
    if START_SOUND:
        try:
            START_SOUND.set_volume(volume)
        except Exception as e:
            print("Failed to set START_SOUND volume:", e)

    GAME_MUSIC = _load(f"Assets/{folder}/sounds/game_music.mp3")
    if GAME_MUSIC:
        try:
            GAME_MUSIC.set_volume(volume)
        except Exception as e:
            print("Failed to set GAME_MUSIC volume:", e)

    WINNER_MUSIC = _load(f"Assets/{folder}/sounds/winner.mp3")
    if WINNER_MUSIC:
        try:
            WINNER_MUSIC.set_volume(volume)
        except Exception as e:
            print("Failed to set WINNER_MUSIC volume:", e)


def reload_sounds(play_menu_after=True):
    """Stop current menu, re-init sounds (reads settings) and optionally play menu music.
    Use this after changing settings.json (folder/volume/sound).
    """
    try:
        stop_menu()
    except Exception:
        pass
    init_sound()
    if play_menu_after:
        try:
            play_menu(loop=True)
        except Exception:
            pass


def play_pop():
    if not sound_on or not mixer_available:
        return
    try:
        if POP_SOUND:
            POP_SOUND.play()
    except Exception as e:
        print("play_pop failed:", e)


def play_menu(loop=True):
    if not sound_on or not mixer_available:
        return
    try:
        if MENU_SOUND:
            MENU_SOUND.play(loops=-1 if loop else 0)
    except Exception as e:
        print("play_menu failed:", e)


def stop_menu():
    if not mixer_available:
        return
    try:
        if MENU_SOUND:
            MENU_SOUND.stop()
    except Exception as e:
        print("stop_menu failed:", e)


def play_start():
    if not sound_on or not mixer_available:
        return
    try:
        if START_SOUND:
            START_SOUND.play()
    except Exception as e:
        print("play_start failed:", e)


def play_game_music(loop=True):
    if not sound_on or not mixer_available:
        return
    try:
        if GAME_MUSIC:
            GAME_MUSIC.play(loops=-1 if loop else 0)
    except Exception as e:
        print("play_game_music failed:", e)


def stop_game_music():
    if not mixer_available:
        return
    try:
        if GAME_MUSIC:
            GAME_MUSIC.stop()
    except Exception as e:
        print("stop_game_music failed:", e)


def play_winner_music(loop=True):
    if not sound_on or not mixer_available:
        return
    try:
        if WINNER_MUSIC:
            WINNER_MUSIC.play(loops=-1 if loop else 0)
    except Exception as e:
        print("play_winner_music failed:", e)


def stop_winner_music():
    if not mixer_available:
        return
    try:
        if WINNER_MUSIC:
            WINNER_MUSIC.stop()
    except Exception as e:
        print("stop_winner_music failed:", e)