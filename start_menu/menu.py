from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def afficher_credit():
    messagebox.showinfo("Credits", "Developed by NPone29 and EscorpionTheo.")

def open_setting(root):
    import start_menu.setting as setting
    setting.run_settings(root)

def open_othello(root):
    root.destroy()
    import gfx
    gfx.run_othello()

def afficher_menu():
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

    play_button = Button(root, text="Play", width=15, height=2, command=lambda: open_othello(root))
    play_button.place(relx=0.5, rely=0.4, anchor="n")

    credit_button = Button(root, text="Credit", width=15, height=2, command=afficher_credit)
    credit_button.place(relx=0.5, rely=0.5, anchor="n")

    setting_button = Button(root, text="Setting", width=15, height=2, command=lambda: open_setting(root))
    setting_button.place(relx=0.5, rely=0.6, anchor="n")

    root.mainloop()