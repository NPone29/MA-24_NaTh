from tkinter import messagebox
# Title : template tkinter
# author : Théo Läderach
# Date : jj.mm.aaaa
# Version : 1.0

from tkinter import *

main=Tk()
main.title("titre de la fenêtre")
main.geometry("400x300")

Button(text="msgbox", command=lambda:print(messagebox.askyesnocancel("yes no", "yes or no"))).pack()
main.mainloop()
