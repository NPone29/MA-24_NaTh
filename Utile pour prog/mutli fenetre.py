
# Title : template tkinter
# author : Théo Läderach
# Date : jj.mm.aaaa
# Version : 1.0

from tkinter import *
page = 0
def change_page():
    global page
    fr_0.pack_forget()
    fr_1.pack_forget()
    fr_2.pack_forget()
    if page == 0:
        fr_0.pack()
        page =1
    elif page == 1:
        fr_1.pack()
        page =2
    elif page == 2:
        fr_2.pack()
        page =0
    print(page)

main=Tk()
main.title("titre de la fenêtre")
main.geometry("400x300")

btn = Button(main,text="change page",command=change_page)
btn.pack()

fr_0 = Frame(main)
text0=Label(fr_0,text="page 1", bg="blue")
text0.pack()

fr_1 = Frame(main)
text1=Label(fr_1,text="page 2", bg="red")
text1.pack()

fr_2 = Frame(main)
text2=Label(fr_2,text="page 3", bg="green")
text2.pack()

main.mainloop()