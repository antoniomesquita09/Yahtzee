from tkinter import Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from models.dices.dices import rollDices, initDices

__all__=[
    'root',
]

def root():
    root = Tk()
    root.geometry("400x400")
    root.title("Jogo")

    labelFactory(root)

    b1 = Button(root, text = "Lancar Dados", activeforeground = "yellow", activebackground = "pink", pady = 10)
    b1.config(command=lambda: rollDicesController(root))
    b1.pack(padx=120, pady=30)
    b1.pack(side = BOTTOM)

    root.mainloop()

def labelFactory(root):
    lbDado1 = Label(root, text = "Dado1", width = 12, anchor = "w")
    lbDado1.place(x = 10,y = 10)
    liDado1 = Listbox(root, width = 10,height = 2, selectmode = SINGLE) 
    liDado1.insert(0,"rodar")
    liDado1.insert(1,"manter")
    liDado1.place(x = 75,y = 10)

    lbDado2 = Label(root, text = "Dado2", width = 12, anchor = "w")
    lbDado2.place(x = 10,y = 50)
    liDado2 = Listbox(root, width = 10,height = 2, selectmode = SINGLE) 
    liDado2.insert(0,"rodar")
    liDado2.insert(1,"manter")
    liDado2.place(x = 75,y = 50)

    lbDado3 = Label(root, text = "Dado3", width = 12, anchor = "w")
    lbDado3.place(x = 10, y = 90)
    liDado3 = Listbox(root, width = 10,height = 2, selectmode = SINGLE) 
    liDado3.insert(0, "rodar")
    liDado3.insert(1, "manter")
    liDado3.place(x = 75, y = 90)

    lbDado4 = Label(root, text = "Dado4", width = 12, anchor = "w")
    lbDado4.place(x = 10, y = 130)
    liDado4 = Listbox(root, width = 10,height = 2, selectmode = SINGLE) 
    liDado4.insert(0,"rodar")
    liDado4.insert(1,"manter")
    liDado4.place(x = 75, y = 130)

    lbDado5 = Label(root, text = "Dado5", width = 12, anchor = "w")
    lbDado5.place(x = 10, y = 170)
    liDado5 = Listbox(root, width = 10,height = 2, selectmode = SINGLE) 
    liDado5.insert(0,"rodar")
    liDado5.insert(1,"manter")
    liDado5.place(x = 75, y = 170)
    return

def rollDicesController(root):
    dices = initDices()
    rollDices(dices, 0)
    imageList = createCanvas(dices, root)
    dicesCanvas(root, imageList)
    return

def dicesCanvas(root, imageList):
    box = Toplevel(root)
    box.title("Lançamento dos Dados")
    box.geometry("300x300")

    canvas = Canvas(box, width=300, height=200, bg="White")

    x=20
    for i in range(0, 5):
        canvas.create_image(x, 20, anchor=NW, image=imageList[i])
        x = x + 40

    canvas.pack()

    bc = Button(box, text = "Fechar", activeforeground = "yellow", activebackground = "pink", pady = 10)
    bc.config(command = lambda: closeWindow(box))
    bc.pack(padx=120, pady=30)
    bc.pack(side = BOTTOM)

    box.update()
    return

def createCanvas(dices, root):
    img = []
    for i in dices:
        if i == 1:
            img.append(PhotoImage(file="assets/dado_1.png"))
        elif i == 2:
            img.append(PhotoImage(file="assets/dado_2.png"))
        elif i == 3:
            img.append(PhotoImage(file="assets/dado_3.png"))
        elif i == 4:
            img.append(PhotoImage(file="assets/dado_4.png"))
        elif i == 5:
            img.append(PhotoImage(file="assets/dado_5.png"))
        elif i == 6:
            img.append(PhotoImage(file="assets/dado_6.png"))
    root.img = img
    return img

def closeWindow(box):
    box.destroy()
