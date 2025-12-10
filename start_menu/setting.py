from tkinter import *
from tkinter import messagebox
import json

def run_settings(parent=None):
    
    if parent is None:
        win = Tk()
        own_mainloop = True #Code générer par copilot pour pouvoir éviter que le script s'arrète : comment faire pour que le menu ne s'arrète pas si j'aimerai aller 2 fois dans les settings ?
    else:
        win = Toplevel(parent)
        own_mainloop = False

    win.title("Othello Setting")
    win.geometry("300x350")

    case_label = Label(win, text="The size of the board (number of squares per side):")
    case_label.pack()

    # Label pour afficher la valeur sélectionnée
    value_label = Label(win, text="Valeur sélectionnée : 0")
    value_label.pack()

    def afficher_valeur(valeur):
        value_label.config(text=f"Value selected: {int(float(valeur))}")

    scale = Scale(win, from_=4, to=20, orient="horizontal", length=300, command=afficher_valeur)

    current_value_size = json.load(open("settings.json")).get("BOARD_WIDTH",8)
    scale.set(current_value_size)
    afficher_valeur(scale.get())
    scale.pack(pady=20)

    background_label = Label(win, text="Choose your background:")
    background_label.pack()

    current_background = json.load(open("settings.json")).get("BACKGROUND_IMAGE_PATH", "Assets/background.png")
    if current_background == "Assets/backgrounds/background.png":
        choix_value = "default"
    elif current_background == "Assets/backgrounds/flowery_background.png":
        choix_value = "flowerly"
    elif current_background == "Assets/backgrounds/sky_background.png":
        choix_value = "sky"
    else:
        choix_value = "space"

    choix = StringVar(value=choix_value)

    radio1 = Radiobutton(win, text="Default", variable=choix, value="default")
    radio2 = Radiobutton(win, text="Flowerly", variable=choix, value="flowerly")
    radio3 = Radiobutton(win, text="Sky", variable=choix, value="sky")
    radio4 = Radiobutton(win, text="Space", variable=choix, value="space")

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    current_sound = json.load(open("settings.json")).get("sound", 0)
    sound = IntVar(value=current_sound)
    check = Checkbutton(win, text="Sound", variable=sound)
    check.pack(pady=10)

    def valider():
        board_size = int(scale.get())
        selected_background = choix.get()
        sound_option = 1 if sound.get() else 0
        messagebox.showinfo("Settings", f"Board Size: {board_size}\nSelected background: {selected_background}\nSound option: {sound_option}")
        import json
        config = {
            "BOARD_WIDTH": board_size,
            "BOARD_HEIGHT": board_size,
            "BACKGROUND_IMAGE_PATH": "Assets/backgrounds/background.png" if selected_background == "default" else "Assets/backgrounds/flowery_background.png" if selected_background == "flowerly" else "Assets/backgrounds/sky_background.png" if selected_background == "sky" else "Assets/backgrounds/space_background.png",
            "TILE_SIZE": 100 if board_size <= 10 else 50,
            "sound": sound.get(),
            "LINE_COLOR": (255, 255, 255) if selected_background == "space" else (0, 0, 0)
        }
        with open("settings.json", 'w') as json_file:
            json.dump(config, json_file)
        import sound as sd
        sd.init_sound()

        win.destroy()  # ferme uniquement la fenêtre de settings

    validate_button = Button(win, text="Validate", command=valider)
    validate_button.pack(pady=20)

    if own_mainloop:
        win.mainloop()
