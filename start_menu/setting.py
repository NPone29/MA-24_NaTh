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
    win.geometry("300x450")

    def set_glitch_mode():
        status = messagebox.askyesno("Glitch Mode", "Are you sure you want to enable glitch mode? This may cause unexpected behavior.")
        if not status:
            return
        # charger la config existante (si elle existe), puis modifier les clefs voulues
        try:
            with open("settings.json", "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            cfg = {}
        # mettre à jour uniquement les valeurs nécessaires
        cfg.update({
            "BACKGROUND_IMAGE_NAME": "Assets/glitch/background.png",
            "TILE_SIZE": 100,
            "LINE_COLOR": [255, 0, 255],
            # ne change pas BOARD_WIDTH/HEIGHT si tu ne veux pas les écraser ici
        })
        with open("settings.json", "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=4, ensure_ascii=False)
        messagebox.showinfo("Glitch Mode", "Glitch mode has been enabled. Please restart the game for changes to take effect.")


    glitch_button = Button(win, command=lambda: set_glitch_mode())
    glitch_button.place(x=0, y=0, width=5, height=5)

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

    current_background = json.load(open("settings.json")).get("BACKGROUND_IMAGE_NAME", "Assets/background.png")
    if current_background == "default_background.png":
        choix_value = "default"
    elif current_background == "flowery_background.png":
        choix_value = "flowery"
    elif current_background == "sky_background.png":
        choix_value = "sky"
    else:
        choix_value = "space"

    choix = StringVar(value=choix_value)

    radio1 = Radiobutton(win, text="Default", variable=choix, value="default")
    radio2 = Radiobutton(win, text="Flowerly", variable=choix, value="flowery")
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
        sound_value_label.config(text=f"Sound: {int(float(valeur))} %")

    volume_scale = Scale(win, from_=0, to=100, orient="horizontal", length=300, command=afficher_valeur_sound)

    current_volume = json.load(open("settings.json")).get("volume", 0)
    current_volume = int(current_volume * 100)
    volume_scale.set(current_volume)
    afficher_valeur_sound(volume_scale.get())
    volume_scale.pack(pady=20)

    current_music = json.load(open("settings.json")).get("music", 1)

    music_var = IntVar(value=current_music)

    music_checkbutton = Checkbutton(win, text="Music", variable=music_var)
    music_checkbutton.place(x=80, y=350)

    current_sound = json.load(open("settings.json")).get("sound", 1)
    sound_var = IntVar(value=current_sound)
    sound_checkbutton = Checkbutton(win, text="Sound", variable=sound_var)
    sound_checkbutton.place(x=165, y=350)

    def show_art_mode():
        art_checkbutton.place(x=125, y=375)
    art = json.load(open("settings.json")).get("art_mode", 0)
    art_mode = IntVar(value=art)
    art_checkbutton = Checkbutton(win, text="Art Mode", variable=art_mode)

    # Event-driven check for Art Mode (ne bloque pas l'UI)
    def check_art_mode(*args):
        if int(volume_scale.get()) == 32 and music_var.get() == 0 and sound_var.get() == 1:
            show_art_mode()
        else:
            try:
                art_checkbutton.place_forget()
            except Exception:
                pass

    check_art_mode()
    # Scale passe la valeur en argument ; trace_add passe (name, index, mode)
    volume_scale.config(command=lambda v: (afficher_valeur_sound(v), check_art_mode()))
    music_var.trace_add("write", lambda *args: check_art_mode())
    sound_var.trace_add("write", lambda *args: check_art_mode())

    def valider():
        board_size = int(case_scale.get())
        selected_background = choix.get()
        volume_option = int(volume_scale.get())
        music_option = music_var.get()
        sound_option = sound_var.get()
        status = messagebox.askyesnocancel("Settings", f"Here are the current settings\n\nBoard Size: {board_size}\nSelected background: {selected_background}\nVolume option: {volume_option}%\nMusic: {'On' if music_option == 1 else 'Off'}\nSound: {'On' if sound_option == 1 else 'Off'}\n\nDo you want to save these settings?")
        if status is True:
            # charge la config actuelle, modifie seulement les clefs voulues
            try:
                with open("settings.json", "r", encoding="utf-8") as f:
                    cfg = json.load(f)
            except Exception:
                cfg = {}
            cfg.update({
                "BOARD_WIDTH": board_size,
                "BOARD_HEIGHT": board_size,
                "TITLE_SIZE": 100 if board_size <= 8 else 50,
                "BACKGROUND_IMAGE_NAME": f"{selected_background}_background.png",
                "volume": volume_option / 100,
                "music": music_option,
                "sound": sound_option,
                "LINE_COLOR": [255, 255, 255] if selected_background == "space" else [0, 0, 0],
                "folder": "default" if art_mode.get() == 0 else "paint texture",
                "art_mode": art_mode.get()
            })
            with open("settings.json", "w", encoding="utf-8") as json_file:
                json.dump(cfg, json_file, indent=4, ensure_ascii=False)
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
        volume_scale.set(50)
        afficher_valeur_sound(volume_scale.get())
        music_var.set(1)
        sound_var.set(1)

    reset_button = Button(btn_frame, text="Reset", command=lambda: reset_to_default(), bg="tomato", activebackground="red3")
    reset_button.pack(side=LEFT, padx=10, pady=0, ipadx=10, ipady=5)

    if own_mainloop:
        win.mainloop()
