from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from models.dices.dices import rollDices

__all__=[
    'createLabel',
]

def createLabel(root, dices):
    lbDado1 = Label(root, text = "Dado1", width = 12, anchor = "w")
    lbDado1.place(x = 10,y = 10)
    maintain1 = IntVar()
    c1 =  Checkbutton(root, text="manter", variable = maintain1)
    c1.place(x = 75 ,y = 10)

    lbDado2 = Label(root, text = "Dado2", width = 12, anchor = "w")
    lbDado2.place(x = 10,y = 50)
    maintain2 = IntVar()
    c2 =  Checkbutton(root, text="manter", variable = maintain2)
    c2.place(x = 75 ,y = 50)

    lbDado3 = Label(root, text = "Dado3", width = 12, anchor = "w")
    lbDado3.place(x = 10, y = 90)
    maintain3 = IntVar()
    c3 =  Checkbutton(root, text="manter", variable = maintain3)
    c3.place(x = 75 ,y = 90)

    lbDado4 = Label(root, text = "Dado4", width = 12, anchor = "w")
    lbDado4.place(x = 10, y = 130)
    maintain4 = IntVar()
    c4 =  Checkbutton(root, text="manter", variable = maintain4)
    c4.place(x = 75 ,y = 130)

    lbDado5 = Label(root, text = "Dado5", width = 12, anchor = "w")
    lbDado5.place(x = 10, y = 170)
    maintain5 = IntVar()
    c5 =  Checkbutton(root, text="manter", variable = maintain5)
    c5.place(x = 75 ,y = 170)

    b1 = Button(root, text = "Lancar Dados", activeforeground = "yellow", activebackground = "pink", pady = 10)
    b1.config(command=lambda: rollDicesController( root, dices, maintain5.get(), maintain4.get(), maintain3.get(), maintain2.get(), maintain1.get()))
    b1.pack(padx=120, pady=30)
    b1.pack(side = BOTTOM)
    b1.place(x = 25 , y = 300)


def rollDicesController(root, dices, dice5, dice4, dice3, dice2, dice1):
    FixNumber = dice5 + dice4*10 + dice3*100 + dice2*1000 + dice1*10000
    rollDices(dices,FixNumber)
    imageList = createCanvas(dices, root)
    dicesCanvas(root, imageList)
    return

def dicesCanvas(root, imageList):
    box = Toplevel(root)
    box.title("Lançamento dos Dados")
    box.geometry("300x300")

    canvas = Canvas(box, width=300, height=200, bg="White")

    x = 20
    for i in range(0, 5):
        canvas.create_image(x, 20, anchor = NW, image = imageList[i])
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
