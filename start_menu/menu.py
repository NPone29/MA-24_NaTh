from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import json

import sound

sound.init_sound()

def afficher_credit():
    if messagebox.askyesno("Credits", "Developed by NPone29 and EscorpionTheo.\nWould you like to buy us a coffee ?") :
        webbrowser.open("https://buymeacoffee.com/npone29")

def open_setting(root):
    import start_menu.setting as setting
    setting.run_settings(root)

def open_othello(root,player_vs_ai=False,level="easy",starting_player=None):
    sound.play_start()
    sound.stop_menu()
    root.destroy()
    sound.init_sound()
    print(starting_player)
    import gfx
    gfx.run_othello(player_vs_ai,level,starting_player=starting_player)


def leave():
    if messagebox.askyesno("do you want to leave?","Do you really want to quit the game?"):
        exit()
        import sys
        sys.exit()

def page(page_name):
    global main_frame,chose_play_frame,chose_level_frame,root
    from start_menu import setting
    
    main_frame.pack_forget()
    chose_play_frame.pack_forget()
    chose_level_frame.pack_forget()

    if page_name=="main":
        main_frame.pack(fill=BOTH, expand=True)
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

def afficher_menu():
    global main_frame,chose_play_frame,chose_level_frame,root
    sound.play_menu(loop=True)
    root = Tk()
    root.title("Othello Menu")
    root.geometry("450x500")
    import core
    core.init_core()
    folder= json.load(open("settings.json")).get("folder","default")
    original_image = Image.open(f"Assets/{folder}/backgrounds/menu_background.png")
    bg_resized = original_image.resize((450, 500), Image.LANCZOS)
    bg = ImageTk.PhotoImage(bg_resized)

    main_frame = Frame(root, bg="", bd=0)
    main_frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(main_frame, width=350, height=400, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg, anchor="nw")
    main_frame._bg_image = bg


    play_button = Button(main_frame, text="Play", width=15, height=2, command=lambda: page("chose_play"), bg="green2", activebackground="green3")
    play_button.place(relx=0.5, rely=0.4, anchor="n")

    credit_button = Button(main_frame, text="Credit", width=15, height=2, command=afficher_credit, bg="deep sky blue", activebackground="dodger blue")
    credit_button.place(relx=0.5, rely=0.5, anchor="n")

    setting_button = Button(main_frame, text="Setting", width=15, height=2, command=lambda: page("settings"), bg="orange2", activebackground="orange3")
    setting_button.place(relx=0.5, rely=0.6, anchor="n")

    leave_button = Button(main_frame, text="Leave", width=15, height=2, command=leave,bg="red2", activebackground="red3")
    leave_button.place(relx=0.5, rely=0.7, anchor="n")


    chose_play_frame = Frame(root, bg="", bd=0)
    canvas2 = Canvas(chose_play_frame, width=350, height=400, highlightthickness=0)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg, anchor="nw")
    chose_play_frame._bg_image = bg

    play_pvp_button = Button(chose_play_frame, text="Player vs Player", width=20, height=2, command=lambda: open_othello(root,player_vs_ai=False,starting_player=whoplay_radio_var.get()), bg="cyan", activebackground="dark turquoise")
    play_pvp_button.place(relx=0.5, rely=0.4, anchor="n")
    play_pvai_button = Button(chose_play_frame, text="Player vs AI", width=20, height=2, command=lambda: page("chose_level"), bg="gold", activebackground="dark goldenrod1")
    play_pvai_button.place(relx=0.5, rely=0.5, anchor="n")
    back_button = Button(chose_play_frame, text="Back", width=10, height=2, command=lambda: page("main"), bg="red2", activebackground="red3")
    back_button.place(relx=0.5, rely=0.8, anchor="n")

    whoplay_txt = Label(chose_play_frame, text="Who start to play ?", font=("Arial", 10),bg="lawn green")
    whoplay_txt.place(relx=0.5, rely=0.6, anchor="n")
    whoplay_radio_var = StringVar(value="rdm")
    whoplay_radio_blue = Radiobutton(chose_play_frame, text="Blue", variable=whoplay_radio_var, value="blue", state=NORMAL,bg="green yellow", activebackground="yellow green")
    whoplay_radio_blue.place(relx=0.45, rely=0.65, anchor="n")
    whoplay_radio_red = Radiobutton(chose_play_frame, text="Red", variable=whoplay_radio_var, value="red", state=NORMAL,bg="green yellow", activebackground="yellow green")
    whoplay_radio_red.place(relx=0.55, rely=0.65, anchor="n")
    whoplay_radio_rdm = Radiobutton(chose_play_frame, text="Random", variable=whoplay_radio_var, value="rdm", state=NORMAL,bg="green yellow", activebackground="yellow green")
    whoplay_radio_rdm.place(relx=0.5, rely=0.7, anchor="n")

    chose_level_frame = Frame(root, bg="", bd=0)
    canvas2 = Canvas(chose_level_frame, width=350, height=400, highlightthickness=0)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg, anchor="nw")
    chose_level_frame._bg_image = bg

    level_easy_button = Button(chose_level_frame, text="Easy", width=20, height=2, command=lambda: open_othello(root,player_vs_ai=True,level="easy",starting_player=whoplay_radio_var.get()), bg="green2", activebackground="green3")
    level_easy_button.place(relx=0.5, rely=0.4, anchor="n")
    level_hard_button = Button(chose_level_frame, text="Hard", width=20, height=2, command=lambda: open_othello(root,player_vs_ai=True,level="hard",starting_player=whoplay_radio_var.get()), bg="orange red", activebackground="OrangeRed3")
    level_hard_button.place(relx=0.5, rely=0.5, anchor="n")
    back_button = Button(chose_level_frame, text="Back", width=10, height=2, command=lambda: page("chose_play"), bg="red2", activebackground="red3")
    back_button.place(relx=0.5, rely=0.7, anchor="n")

    root.mainloop()