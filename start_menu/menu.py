from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

import sound

sound.init_sound()

def afficher_credit():
    if messagebox.askyesno("Credits", "Developed by NPone29 and EscorpionTheo.\nWould you like to buy us a coffee ?") :
        webbrowser.open("https://buymeacoffee.com/")

def open_setting(root):
    import start_menu.setting as setting
    setting.run_settings(root)

def open_othello(root):
    sound.play_start()
    sound.stop_menu()
    root.destroy()
    import gfx
    gfx.run_othello()
    sound.init_sound()


def leave():
    if messagebox.askyesno("do you want to leave?","Do you really want to quit the game?"):
        exit()
        import sys
        sys.exit()

def afficher_menu():
    sound.play_menu(loop=True)
    root = Tk()
    root.title("Othello Menu")
    root.geometry("450x500")

    original_image = Image.open("Assets/backgrounds/menu_background.png")
    bg_resized = original_image.resize((450, 500), Image.LANCZOS)
    bg = ImageTk.PhotoImage(bg_resized)

    canvas = Canvas(root, width=350, height=400, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg, anchor="nw")
    root._bg_image = bg

    play_button = Button(root, text="Play", width=15, height=2, command=lambda: open_othello(root), bg="green2", activebackground="green3")
    play_button.place(relx=0.5, rely=0.4, anchor="n")

    credit_button = Button(root, text="Credit", width=15, height=2, command=afficher_credit, bg="deep sky blue", activebackground="dodger blue")
    credit_button.place(relx=0.5, rely=0.5, anchor="n")

    setting_button = Button(root, text="Setting", width=15, height=2, command=lambda: open_setting(root), bg="orange2", activebackground="orange3")
    setting_button.place(relx=0.5, rely=0.6, anchor="n")

    leave_button = Button(root, text="Leave", width=15, height=2, command=leave,bg="red2", activebackground="red3")
    leave_button.place(relx=0.5, rely=0.7, anchor="n")

    root.mainloop()