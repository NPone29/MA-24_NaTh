from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import json
from utils import resource_path
import sound
import sys

###############################################################################



def afficher_credit(): # Fonction qui affiche les crédits
    if messagebox.askyesno("Credits","""Developed by NPone29 and EscorpionTheo.
                           Would you like to buy us a coffee ?""") :
        webbrowser.open("https://buymeacoffee.com/npone29")

def open_setting(root): # fonction qui va remplacer afficher la page du menu
    import start_menu.setting as setting
    setting.run_settings(root)

#fonction qui va lancer le jeu avec les arguments de lancement
def open_othello(root, player_vs_ai=False, level="easy", starting_player=None):
    import sound
    try:
        sound.stop_menu()
    except Exception:
        pass

    # destroy Tk main window before running pygame
    try:
        root.destroy()
    except Exception:
        pass

    try:
        import gfx
        reopen = gfx.run_othello(player_vs_ai, level, starting_player=starting_player)
    except Exception as e:
        # print stack trace so you can debug the .exe crash
        import traceback, sys
        print("Exception while running gfx.run_othello():", e, file=sys.stderr)
        traceback.print_exc()
        reopen = False

    if reopen:
        # re-init sound subsystem safely and relaunch the menu
        try:
            sound.init_sound()
            sound.play_menu(loop=True)
        except Exception:
            pass
        try:
            afficher_menu()
        except Exception as e:
            import traceback, sys
            print("Failed to reopen menu:", e, file=sys.stderr)
            traceback.print_exc()

#fonction qui va fermer le programme avec une pop-up de validation
def leave():
    if messagebox.askyesno("do you want to leave?",
                           "Do you really want to quit the game?"):
        try:
            sound.stop_menu()
        except Exception:
            pass
        try:
            root.destroy()
        except Exception:
            pass
        try:
            sys.exit(0)
        except Exception:
            try:
                import os
                os._exit(0)
            except Exception:
                pass



#fonction qui affiche une page correspondant à l'argument
def page(page_name):
    global main_frame,chose_play_frame,chose_level_frame,root
    from start_menu import setting
    
    main_frame.pack_forget()
    chose_play_frame.pack_forget()
    chose_level_frame.pack_forget()

    if page_name=="main":
        main_frame.pack(fill=BOTH, expand=True)
        setting.settings_frame.pack_forget()
        print("main page")
    elif page_name=="chose_play":
        chose_play_frame.pack(fill=BOTH, expand=True)
        print("chose play page")
    elif page_name=="chose_level":
        chose_level_frame.pack(fill=BOTH, expand=True)
        print("chose level page")
    elif page_name=="settings":
        setting.run_settings(root).pack(fill=BOTH, expand=True)
        print("settings page")

# fonction qui va afficher tout le menu
def afficher_menu():
    global main_frame,chose_play_frame,chose_level_frame,root
    sound.init_sound()
    sound.play_menu(loop=True)
    root = Tk()
    root.title("Othello Menu")
    root.geometry("450x500")
    root.iconbitmap(resource_path("Assets\icon.ico"))
    import core
    core.init_core()
    folder= json.load(open("settings.json")).get("folder","default")
    original_image = Image.open(
        resource_path(f"Assets/{folder}/backgrounds/menu_background.png"))
    bg_resized = original_image.resize((450, 500), Image.LANCZOS)
    bg = ImageTk.PhotoImage(bg_resized)

    main_frame = Frame(root, bg="", bd=0)
    main_frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(main_frame, width=350, height=400, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg, anchor="nw")
    main_frame._bg_image = bg


    play_button = Button(main_frame, text="Play", width=15, height=2,
                        command=lambda: page("chose_play"), bg="green2", 
                        activebackground="green3")
    play_button.place(relx=0.5, rely=0.4, anchor="n")

    credit_button = Button(main_frame, text="Credit", width=15, height=2, 
                           command=afficher_credit, bg="deep sky blue", 
                           activebackground="dodger blue")
    credit_button.place(relx=0.5, rely=0.5, anchor="n")

    setting_button = Button(main_frame, text="Setting", width=15, height=2, 
                            command=lambda: page("settings"), bg="orange2", 
                            activebackground="orange3")
    setting_button.place(relx=0.5, rely=0.6, anchor="n")

    leave_button = Button(main_frame, text="Leave", width=15, height=2, 
                          command=leave,bg="red2", activebackground="red3")
    leave_button.place(relx=0.5, rely=0.7, anchor="n")


    chose_play_frame = Frame(root, bg="", bd=0)
    canvas2 = Canvas(chose_play_frame, width=350, height=400, 
                     highlightthickness=0)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg, anchor="nw")
    chose_play_frame._bg_image = bg

    play_pvp_button = Button(chose_play_frame, text="Player vs Player", 
                            width=20, height=2,bg="cyan",
                                        activebackground="dark turquoise",
                                        command=lambda: 
                                        open_othello(root,
                                                     player_vs_ai=False,
                                                     starting_player=whoplay_radio_var.get()
                                                     ))
    play_pvp_button.place(relx=0.5, rely=0.4, anchor="n")
    play_pvai_button = Button(chose_play_frame, text="Player vs AI",
                              width=20, height=2, command=lambda: 
                              page("chose_level"), bg="gold",
                              activebackground="dark goldenrod1")
    play_pvai_button.place(relx=0.5, rely=0.5, anchor="n")
    back_button = Button(chose_play_frame, text="Back", width=10, height=2, 
                         command=lambda: page("main"), bg="red2", 
                         activebackground="red3")
    back_button.place(relx=0.5, rely=0.8, anchor="n")

    whoplay_txt = Label(chose_play_frame, text="Who start to play ?", 
                        font=("Arial", 10),bg="lawn green")
    whoplay_txt.place(relx=0.5, rely=0.6, anchor="n")
    whoplay_radio_var = StringVar(value="rdm")
    whoplay_radio_blue = Radiobutton(chose_play_frame, text="Blue",
                                     variable=whoplay_radio_var, value="blue",
                                     state=NORMAL,bg="green yellow",
                                     activebackground="yellow green")
    whoplay_radio_blue.place(relx=0.45, rely=0.65, anchor="n")
    whoplay_radio_red = Radiobutton(chose_play_frame, text="Red", 
                                    variable=whoplay_radio_var, value="red", 
                                    state=NORMAL,bg="green yellow",
                                    activebackground="yellow green")
    whoplay_radio_red.place(relx=0.55, rely=0.65, anchor="n")
    whoplay_radio_rdm = Radiobutton(chose_play_frame, text="Random",
                                    variable=whoplay_radio_var,
                                    value="rdm", state=NORMAL,
                                    bg="green yellow", 
                                    activebackground="yellow green")
    whoplay_radio_rdm.place(relx=0.5, rely=0.7, anchor="n")

    chose_level_frame = Frame(root, bg="", bd=0)
    canvas2 = Canvas(chose_level_frame, width=350, height=400,
                     highlightthickness=0)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg, anchor="nw")
    chose_level_frame._bg_image = bg

    level_easy_button = Button(chose_level_frame, text="Easy",
                               width=20, height=2, bg="green2",
                               activebackground="green3",
                               command=lambda:
                               open_othello(root,
                                            player_vs_ai=True,
                                            level="easy",
                                            starting_player=whoplay_radio_var.get()
                                            ))
    level_easy_button.place(relx=0.5, rely=0.4, anchor="n")
    level_hard_button = Button(chose_level_frame, text="Hard", 
                               width=20, height=2, bg="orange red",
                                 activebackground="OrangeRed3", 
                                 command=lambda:
                                 open_othello(root,player_vs_ai=True,
                                            level="hard",
                                            starting_player=whoplay_radio_var.get()
                                            ))
    level_hard_button.place(relx=0.5, rely=0.5, anchor="n")
    back_button = Button(chose_level_frame, text="Back", width=10, height=2,
                         command=lambda: page("chose_play"), bg="red2", 
                         activebackground="red3")
    back_button.place(relx=0.5, rely=0.7, anchor="n")


    root.mainloop()