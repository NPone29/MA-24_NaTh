from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Othello Menu")
root.geometry("350x400")

image_frame = Frame(root, height=300)
image_frame.pack(side=TOP, fill=X)

button_frame = Frame(root, height=100)
button_frame.pack(side=TOP, fill=X, pady=10)



# image = PhotoImage(file="path/to/image.png")  # renseigner le chemin si besoin
# label = Label(root, image=image)
# label.pack()

def afficher_credit():
    messagebox.showinfo("Credits", "Ton texte de crédits ici")

def setting():
    global root
    root.destroy()
    import start_menu.setting as setting
    setting.run_settings()

def othello():
    global root
    root.destroy()   
    import gfx
    gfx.run_othello()


def afficher_menu():
    credit_button = Button(button_frame, text="Credit", width=10, height=3, command=afficher_credit)
    credit_button.pack(side=LEFT, expand=True, padx=10, pady=5)

    play_button = Button(button_frame, text="Play",   width=10, height=3, command=othello)
    play_button.pack(side=LEFT,   expand=True, padx=10, pady=5)

    setting_button= Button(button_frame, text="Setting",width=10, height=3, command=setting)
    setting_button.pack(side=LEFT,expand=True, padx=10, pady=5)

    root.mainloop()