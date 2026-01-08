# Title : Script qui gère l'interface des paramètres
# author : pj43svh & NPone29
# Date : 08.01.2026
# Version : 1.2.1

from tkinter import *
from tkinter import messagebox
import json
import subprocess

# fonction qui va définir la frame des settings comme page
def run_settings(parent=None):
    global settings_frame
    settings_frame = Frame(parent)

    # fonction permettant de définir le mode graphique "glitch"
    def set_glitch_mode():
        status = messagebox.askyesno("Glitch Mode",
                                    "Are you sure you want to enable glitch mode?" \
                                    "This may cause unexpected behavior.")
        if not status:
            return
        
        try:
            with open("settings.json", "r", encoding="utf-8") as f:
                cfg = json.load(f)
        except Exception:
            cfg = {}
        
        cfg.update({
            "BACKGROUND_IMAGE_NAME": "glitch_background.png",
            "TILE_SIZE": 100,
            "LINE_COLOR": [255, 0, 255],
            "folder": "glitch",
            "art_mode": 0,
            "glitch_mode": 1
        })
        with open("settings.json", "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=4, ensure_ascii=False)
        messagebox.showwarning("Glitch Mode", 
                            "Glitch mode has been enabled. " \
                            "The game will now restart to apply the changes." \
                            " If it does not restart automatically, " \
                            "please restart it manually.")
        import sound as sd
        sd.stop_menu()
        sd.init_sound()
        parent.destroy()
        subprocess.run(["python", "main.py"])


    glitch_button = Button(settings_frame, command=lambda: set_glitch_mode())
    glitch_button.place(x=0, y=0, width=5, height=5)

    case_label = Label(settings_frame,text=
                       "The size of the board (number of squares per side):")
    case_label = Label(settings_frame, text=
                       "The size of the board (number of squares per side):")
    case_label.pack()

    # Label pour afficher la valeur sélectionnée
    case_value_label = Label(settings_frame, text="Value selected: 0")
    case_value_label.pack()

    # fonction qui va afficher la valeur de la taille du plateau.
    def afficher_valeur_case(valeur):
        case_value_label.config(text=f"Value selected: {int(float(valeur))}")

    case_scale = Scale(settings_frame, from_=4, to=20, orient="horizontal",
                       length=300, command=afficher_valeur_case)

    current_value_size = json.load(open("settings.json")).get("BOARD_WIDTH",8)
    case_scale.set(current_value_size)
    afficher_valeur_case(case_scale.get())
    case_scale.pack(pady=20)

    background_label = Label(settings_frame, text="Choose your background:")
    background_label.pack()

    current_background = json.load(open("settings.json")).get(
        "BACKGROUND_IMAGE_NAME", "Assets/background.png")
    if current_background == "default_background.png":
        choix_value = "default"
    elif current_background == "flowery_background.png":
        choix_value = "flowery"
    elif current_background == "sky_background.png":
        choix_value = "sky"
    elif current_background == "space_background.png":
        choix_value = "space"
    else:
        choix_value = "None"

    choix = StringVar(value=choix_value)

    radio1 = Radiobutton(settings_frame, text="Default", variable=choix,
                         value="default")
    radio2 = Radiobutton(settings_frame, text="Flowery", variable=choix,
                         value="flowery")
    radio3 = Radiobutton(settings_frame, text="Sky", variable=choix,
                         value="sky")
    radio4 = Radiobutton(settings_frame, text="Space", variable=choix,
                         value="space")

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    sound_label = Label(settings_frame, text="Adjust the sound level:")
    sound_label.pack()

    sound_value_label = Label(settings_frame, text="Sound: 0")
    sound_value_label.pack()

    #fonction qui va afficher le volume du son
    def afficher_valeur_sound(valeur):
        sound_value_label.config(text=f"Sound: {int(float(valeur))} %")

    volume_scale = Scale(settings_frame, from_=0, to=100, 
                         orient="horizontal", length=300,
                         command=afficher_valeur_sound)

    current_volume = json.load(open("settings.json")).get("volume", 0)
    current_volume = int(current_volume * 100)
    volume_scale.set(current_volume)
    afficher_valeur_sound(volume_scale.get())
    volume_scale.pack(pady=20)

    current_music = json.load(open("settings.json")).get("music", 1)

    music_var = IntVar(value=current_music)

    music_checkbutton = Checkbutton(settings_frame, text="Music",
                                    variable=music_var)
    music_checkbutton.place(relx=0.35, y=350)

    current_sound = json.load(open("settings.json")).get("sound", 1)
    sound_var = IntVar(value=current_sound)
    sound_checkbutton = Checkbutton(settings_frame, text="Sound",
                                    variable=sound_var)
    sound_checkbutton.place(relx=0.55, y=350)

    def show_art_mode():
        art_checkbutton.place(relx=0.45, y=375)
    art = json.load(open("settings.json")).get("art_mode", 0)
    art_mode = IntVar(value=art)
    art_checkbutton = Checkbutton(settings_frame, text="Art Mode",
                                  variable=art_mode)

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
    # Scale passe la valeur en argument ;
    # trace_add passe (name, index, mode)
    volume_scale.config(command=lambda v: 
                        (afficher_valeur_sound(v), check_art_mode()))
    music_var.trace_add("write", lambda *args: check_art_mode())
    sound_var.trace_add("write", lambda *args: check_art_mode())

    # fonction qui va enregistrer les valeurs dans le fichiers json
    def valider():
        board_size = int(case_scale.get())
        selected_background = choix.get()
        volume_option = int(volume_scale.get())
        music_option = music_var.get()
        sound_option = sound_var.get()
        
        from start_menu import menu
        status = messagebox.askyesnocancel("Settings",
                        f"""Here are the current settings

                            Board Size: {board_size}
                            Selected background: {selected_background}
                            Volume option: {volume_option}%
                            Music: {'On' if music_option == 1 else 'Off'}
                            Sound: {'On' if sound_option == 1 else 'Off'}
                            
                            Do you want to save these settings?""")
        if status is True:
            # charge la config actuelle, modifie seulement les clefs voulues
            from core import config
            if  config.get("glitch_mode")==1:
                restart = True
            else:
                restart = False
            try:
                with open("settings.json", "r", encoding="utf-8") as f:
                    cfg = json.load(f)
                

            except Exception:
                cfg = {}
            cfg.update({
                "BOARD_WIDTH": board_size,
                "BOARD_HEIGHT": board_size,
                "TITLE_SIZE": 100 if board_size <= 8 else 50,
                "BACKGROUND_IMAGE_NAME": 
                f"{selected_background}_background.png",
                "volume": volume_option / 100,
                "music": music_option,
                "sound": sound_option,
                "LINE_COLOR": [255, 255, 255] 
                if selected_background == "space" else [0, 0, 0],
                "folder": "default" 
                if art_mode.get() == 0 else "paint texture",
                "art_mode": art_mode.get(),
                "glitch_mode": 0
            })
            with open("settings.json", "w", encoding="utf-8") as json_file:
                json.dump(cfg, json_file, indent=4, ensure_ascii=False)
            import sound as sd
            sd.stop_menu()
            if config.get("art_mode") == 1 or art_mode.get()==1 or restart :
                restart = True
            else:
                restart = False
            if restart:
                messagebox.showwarning("The game will restart",
                                       "The game will restart. If it does not" \
                                       " restart automatically," \
                                       " please restart it manually.")
                parent.destroy()
                subprocess.run(["python", "main.py"])
            else:
                from start_menu import menu
                menu.page("main")
                sd.init_sound()
                sd.play_menu(True)
                

        elif status is False:
            menu.page("main")
            settings_frame.destroy()
        elif status is None:
            pass
    
    btn_frame = Frame(settings_frame, height=20)
    btn_frame.pack(fill=X, side=BOTTOM, pady=10)
    validate_button = Button(btn_frame, text="Validate", command=valider,
                             bg="green2", activebackground="green3")
    validate_button.pack(side=RIGHT, padx=10, pady=0, ipadx=10, ipady=5)

    #fonctio^n qui va rétablir tout les paramètre au valeur par default
    def reset_to_default():
        case_scale.set(8)
        afficher_valeur_case(case_scale.get())
        choix.set("default")
        volume_scale.set(50)
        afficher_valeur_sound(volume_scale.get())
        music_var.set(1)
        sound_var.set(1)
        art_mode.set(0)

    reset_button = Button(btn_frame, text="Reset",
                          command=lambda: reset_to_default(), bg="tomato",
                          activebackground="red3")
    reset_button.pack(side=LEFT, padx=10, pady=0, ipadx=10, ipady=5)
    return settings_frame

