import json
import os
from utils import resource_path


# API publique — fonctions sûres même si mixer indisponible
def init_sound():
    # possibilité de relire settings.json et (ré)initialiser le mixer si dispo
    global _sound_on, _volume, _folder, _mixer_available
    try:
        with open(resource_path("settings.json"), "r", encoding="utf-8") as f:
            cfg = json.load(f)
            _sound_on = cfg.get("sound", 1)
            _volume = cfg.get("volume", 0.5)
            _folder = cfg.get("folder", "default")
    except Exception:
        pass
    # tenter de réinitialiser le mixer si nécessaire
    if not _mixer_available:
        try:
            import pygame
            if getattr(pygame, "mixer", None) is not None:
                try:
                    pygame.mixer.init()
                    # recharger le module et sounds n'est pas fait ici (lazy load on play)
                    _mixer_available = True
                except Exception:
                    _mixer_available = False
        except Exception:
            _mixer_available = False
    
# charger config (assure que settings.json existe avant import)
_config = {}
try:
    with open(resource_path("settings.json"), "r", encoding="utf-8") as _f:
        _config = json.load(_f)
except Exception:
    _config = {}

_sound_on = _config.get("sound", 1)
_volume = _config.get("volume", 0.5)
_folder = _config.get("folder", "default")

# essayer d'importer pygame et d'initialiser le mixer en sécurité
_mixer_available = False
_mixer = None
try:
    import pygame
    try:
        # accéder à pygame.mixer peut lever NotImplementedError dans le bundle
        if getattr(pygame, "mixer", None) is not None:
            try:
                pygame.mixer.init()
                _mixer = pygame.mixer
                _mixer_available = True
            except Exception:
                _mixer_available = False
        else:
            _mixer_available = False
    except Exception:
        _mixer_available = False
except Exception:
    _mixer_available = False

# charger les sounds uniquement si mixer disponible
_POP_SOUND = None
_MENU_SOUND = None
_START_SOUND = None
_GAME_MUSIC = None

if _mixer_available:
    try:
        _POP_SOUND = _mixer.Sound(resource_path(f"Assets/{_folder}/sounds/pop.mp3"))
        _POP_SOUND.set_volume(_volume)
    except Exception:
        _POP_SOUND = None
    try:
        _MENU_SOUND = _mixer.Sound(resource_path(f"Assets/{_folder}/sounds/menu.mp3"))
        _MENU_SOUND.set_volume(_volume)
    except Exception:
        _MENU_SOUND = None
    try:
        _START_SOUND = _mixer.Sound(resource_path(f"Assets/{_folder}/sounds/start.mp3"))
        _START_SOUND.set_volume(_volume)
    except Exception:
        _START_SOUND = None
    try:
        _GAME_MUSIC = _mixer.Sound(resource_path(f"Assets/{_folder}/sounds/game_music.mp3"))
        _GAME_MUSIC.set_volume(_volume)
    except Exception:
        _GAME_MUSIC = None
    try:
        _WINNER_MUSIC = _mixer.Sound(resource_path(f"Assets/{_folder}/sounds/winner.mp3"))
        _WINNER_MUSIC.set_volume(_volume)
    except Exception:
        _WINNER_MUSIC = None
    
def play_pop():
    if not _sound_on or not _mixer_available:
        return
    try:
        if _POP_SOUND:
            _POP_SOUND.play()
    except Exception:
        pass

def play_menu(loop=True):
    if not _sound_on or not _mixer_available:
        return
    try:
        if _MENU_SOUND:
            _MENU_SOUND.play(loops=-1 if loop else 0)
    except Exception:
        pass

def stop_menu():
    if not _mixer_available:
        return
    try:
        if _MENU_SOUND:
            _MENU_SOUND.stop()
    except Exception:
        pass

def play_start():
    if not _sound_on or not _mixer_available:
        return
    try:
        if _START_SOUND:
            _START_SOUND.play()
    except Exception:
        pass

def play_game_music(loop=True):
    if not _sound_on or not _mixer_available:
        return
    try:
        if _GAME_MUSIC:
            _GAME_MUSIC.play(loops=-1 if loop else 0)
    except Exception:
        pass

def stop_game_music():
    if not _mixer_available:
        return
    try:
        if _GAME_MUSIC:
            _GAME_MUSIC.stop()
    except Exception:
        pass
def play_winner_music(loop=True):
    if not _sound_on or not _mixer_available:
        return
    try:
        if _WINNER_MUSIC:
            _WINNER_MUSIC.play(loops=-1 if loop else 0)
    except Exception:
        pass

def stop_winner_music():
    if not _mixer_available:
        return
    try:
        if _WINNER_MUSIC:
            _WINNER_MUSIC.stop()
    except Exception:
        pass