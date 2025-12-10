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
    win.geometry("300x425")

    case_label = Label(win, text="The size of the board (number of squares per side):")
    case_label.pack()

    # Label pour afficher la valeur sélectionnée
    case_value_label = Label(win, text="Value selected: 0")
    case_value_label.pack()

    def afficher_valeur_case(valeur):
        case_value_label.config(text=f"Value selected: {int(float(valeur))}")

    case_scale = Scale(win, from_=4, to=20, orient="horizontal", length=300, command=afficher_valeur_case)

    current_value_size = json.load(open("settings.json")).get("BOARD_WIDTH",8)
    case_scale.set(current_value_size)
    afficher_valeur_case(case_scale.get())
    case_scale.pack(pady=20)

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

    sound_label = Label(win, text="Adjust the sound level:")
    sound_label.pack()

    sound_value_label = Label(win, text="Sound: 0")
    sound_value_label.pack()

    def afficher_valeur_sound(valeur):
        sound_value_label.config(text=f"Sound: {int(float(valeur))}")

    sound_scale = Scale(win, from_=0, to=100, orient="horizontal", length=300, command=afficher_valeur_sound)

    current_sound = json.load(open("settings.json")).get("sound", 0)
    current_sound = int(current_sound * 100)
    sound_scale.set(current_sound)
    afficher_valeur_sound(sound_scale.get())
    sound_scale.pack(pady=20)


    def valider():
        board_size = int(case_scale.get())
        selected_background = choix.get()
        sound_option = int(sound_scale.get())
        status = messagebox.askyesnocancel("Settings", f"Here are the current settings\n\nBoard Size: {board_size}\nSelected background: {selected_background}\nSound option: {sound_option}%")
        if status is True:
            import json
            config = {
                "BOARD_WIDTH": board_size,
                "BOARD_HEIGHT": board_size,
                "BACKGROUND_IMAGE_PATH": "Assets/backgrounds/background.png" if selected_background == "default" else "Assets/backgrounds/flowery_background.png" if selected_background == "flowerly" else "Assets/backgrounds/sky_background.png" if selected_background == "sky" else "Assets/backgrounds/space_background.png",
                "TILE_SIZE": 100 if board_size <= 10 else 50,
                "sound": sound_option / 100,
                "LINE_COLOR": (255, 255, 255) if selected_background == "space" else (0, 0, 0)
            }
            with open("settings.json", 'w') as json_file:
                json.dump(config, json_file)
            import sound as sd
            sd.stop_menu()
            sd.init_sound()
            sd.play_menu(True)
            win.destroy()
        elif status is False:
            win.destroy()
        elif status is None:
            pass
    
    btn_frame = Frame(win, height=20)
    btn_frame.pack(fill=X, side=BOTTOM, pady=10)
    validate_button = Button(btn_frame, text="Validate", command=valider, bg="green2", activebackground="green3")
    validate_button.pack(side=RIGHT, padx=10, pady=0, ipadx=10, ipady=5)

    def reset_to_default():
        case_scale.set(8)
        afficher_valeur_case(case_scale.get())
        choix.set("default")
        sound_scale.set(50)
        afficher_valeur_sound(sound_scale.get())

    reset_button = Button(btn_frame, text="Reset", command=lambda: reset_to_default(), bg="tomato", activebackground="red3")
    reset_button.pack(side=LEFT, padx=10, pady=0, ipadx=10, ipady=5)

    if own_mainloop:
        win.mainloop()
