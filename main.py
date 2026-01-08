# Title : Script qui lance le jeu et crée le fichier de configuration s'il n'existe pas
# author : pj43svh & NPone29
# Date : 08.01.2026
# Version : 1.2.1

import os
import json


#Parameter par defauts
DEFAULT_SETTINGS = {
    "BOARD_WIDTH": 8,
    "BOARD_HEIGHT": 8,
    "TITLE_SIZE": 100,
    "BACKGROUND_IMAGE_NAME": "default_background.png",
    "volume": 0.5,
    "music": 1,
    "sound": 1,
    "LINE_COLOR": [0, 0, 0],
    "folder": "default",
    "art_mode": 0,
    "glitch_mode": 0,
    "TILE_SIZE": 100
}


# Vérification si le ficher settings.json existe,
# sinon le créer avec les paramètres par défaut
def ensure_settings(path="settings.json"):
    if not os.path.exists(path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_SETTINGS, f, indent=4, ensure_ascii=False)
                f.write("\n")
                print("Created default settings.json")
        except Exception as e:
            print("Impossible de créer settings.json :", e)
            exit(1)


# lancement du programme
if __name__ == "__main__":
    ensure_settings(path="settings.json")
    from start_menu import menu
    menu.afficher_menu() #affichage du menu de démarrage

