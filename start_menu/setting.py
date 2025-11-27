from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Othello Setting")
root.geometry("300x350")


case_label = Label(root, text="The size of the board (number of squares per side):")
case_label.pack()

# Label pour afficher la valeur sélectionnée
value_label = Label(root, text="Valeur sélectionnée : 0")
value_label.pack()

def afficher_valeur(valeur):
    value_label.config(text=f"Value selected: {int(float(valeur))}")

scale = Scale(root, from_=4, to=25, orient="horizontal", length=300, command=afficher_valeur)
scale.set(8)
afficher_valeur(scale.get())
scale.pack(pady=20)

background_label = Label(root, text="Choose your background:")
background_label.pack()

choix = StringVar()
choix.set("default")

radio1 = Radiobutton(root, text="Default", variable=choix, value="default")
radio2 = Radiobutton(root, text="Flowerly", variable=choix, value="flowerly")
radio3 = Radiobutton(root, text="Option 3", variable=choix, value="option3")

radio1.pack()
radio2.pack()
radio3.pack()

sound = IntVar()

check = Checkbutton(root, text="Sound", variable=sound)
check.pack(pady=10)

def valider():
    board_size = int(scale.get())
    selected_background = choix.get()
    sound_option = "On" if sound.get() else "Off"
    messagebox.showinfo("Settings", f"Board Size: {board_size}\nSelected background: {selected_background}\nSound option: {sound_option}")

    root.destroy()  # fermer la fenêtre current avant de recréer le menu

    import importlib
    import start_menu.menu as menu
    importlib.reload(menu)  # idée de copilot pour recharger le module (Pourquoi est ce que j'ai cette erreur ?)
    menu.afficher_menu()

validate_button = Button(root, text="Validate", command=valider)
validate_button.pack(pady=20)

def run_settings():
    root.mainloop()
