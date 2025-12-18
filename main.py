import os
import json

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

if __name__ == "__main__":
    ensure_settings(path="settings.json")
    from start_menu import menu
    menu.afficher_menu()

