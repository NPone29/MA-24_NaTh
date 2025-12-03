from tkinter import *
from tkinter import messagebox

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

    scale = Scale(win, from_=4, to=25, orient="horizontal", length=300, command=afficher_valeur)
    scale.set(8)
    afficher_valeur(scale.get())
    scale.pack(pady=20)

    background_label = Label(win, text="Choose your background:")
    background_label.pack()

    choix = StringVar(value="default")

    radio1 = Radiobutton(win, text="Default", variable=choix, value="default")
    radio2 = Radiobutton(win, text="Flowerly", variable=choix, value="flowerly")
    radio3 = Radiobutton(win, text="Option 3", variable=choix, value="option3")

    radio1.pack()
    radio2.pack()
    radio3.pack()

    sound = IntVar(value=1)
    check = Checkbutton(win, text="Sound", variable=sound)
    check.pack(pady=10)

    def valider():
        board_size = int(scale.get())
        selected_background = choix.get()
        sound_option = "On" if sound.get() else "Off"
        messagebox.showinfo("Settings", f"Board Size: {board_size}\nSelected background: {selected_background}\nSound option: {sound_option}")
        import core as c
        c.BOARD_WIDTH = board_size
        c.BOARD_HEIGHT = board_size
        import gfx as g
        if selected_background == "flowerly":
            g.background_image = "./Assets/flowery_background.png"
        else:
            g.background_image = "./Assets/background.png"
        win.destroy()  # ferme uniquement la fenêtre de settings

    validate_button = Button(win, text="Validate", command=valider)
    validate_button.pack(pady=20)

    if own_mainloop:
        win.mainloop()
