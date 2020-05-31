from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from models.dices.dices import rollDices

__all__=[
    'createLabel',
]
countRoll = 0
maintain1 = False
maintain2 = False
maintain3 = False
maintain4 = False
maintain5 = False
maintainNumber = 11111

def callback(event):
    global maintain1
    global maintain2
    global maintain3
    global maintain4
    global maintain5
    global maintainNumber
    print ("clicked at", event.x, event.y)
    if event.y >= 20 and event.y <=50:
        if event.x >= 20 and event.x <=50:
            if not maintain1:
                print("Dado1 marcado")
                maintainNumber -= 10000
            else:
                print("Dado1 desmarcado")
                maintainNumber += 10000
            maintain1 = not maintain1
        if event.x >= 60 and event.x <=90:
            if not maintain2:
                print("Dado2 marcado")
                maintainNumber -= 1000
            else:
                print("Dado2 desmarcado")
                maintainNumber += 1000
            maintain2 = not maintain2
        if event.x >= 100 and event.x <=130:
            if not maintain3:
                print("Dado3 marcado")
                maintainNumber -= 100
            else:
                print("Dado3 desmarcado")
                maintainNumber += 100
            maintain3 = not maintain3
        if event.x >= 140 and event.x <=170:
            if not maintain4:
                print("Dado4 marcado")
                maintainNumber -= 10
            else:
                print("Dado4 desmarcado")
                maintainNumber += 10
            maintain4 = not maintain4
        if event.x >= 180 and event.x <=210:
            if not maintain5:
                print("Dado5 marcado")
                maintainNumber -= 1
            else:
                print("Dado5 desmarcado")
                maintainNumber += 1
            maintain5 = not maintain5
    return

            
def createLabel(root, dices):
    # lbDado1 = Label(root, text = "Dado1", width = 12, anchor = "w")
    # lbDado1.place(x = 10,y = 10)
    # maintain1 = IntVar()
    # c1 =  Checkbutton(root, text="manter", variable = maintain1)
    # c1.place(x = 75 ,y = 10)

    # lbDado2 = Label(root, text = "Dado2", width = 12, anchor = "w")
    # lbDado2.place(x = 10,y = 50)
    # maintain2 = IntVar()
    # c2 =  Checkbutton(root, text="manter", variable = maintain2)
    # c2.place(x = 75 ,y = 50)

    # lbDado3 = Label(root, text = "Dado3", width = 12, anchor = "w")
    # lbDado3.place(x = 10, y = 90)
    # maintain3 = IntVar()
    # c3 =  Checkbutton(root, text="manter", variable = maintain3)
    # c3.place(x = 75 ,y = 90)

    # lbDado4 = Label(root, text = "Dado4", width = 12, anchor = "w")
    # lbDado4.place(x = 10, y = 130)
    # maintain4 = IntVar()
    # c4 =  Checkbutton(root, text="manter", variable = maintain4)
    # c4.place(x = 75 ,y = 130)

    # lbDado5 = Label(root, text = "Dado5", width = 12, anchor = "w")
    # lbDado5.place(x = 10, y = 170)
    # maintain5 = IntVar()
    # c5 =  Checkbutton(root, text="manter", variable = maintain5)
    # c5.place(x = 75 ,y = 170)

    b1 = Button(root, text = "Lancar Dados", activeforeground = "yellow", activebackground = "pink", pady = 10)
    b1.config(command=lambda: rollDicesController( root, dices))
    b1.pack(padx=120, pady=30)
    b1.pack(side = BOTTOM)
    b1.place(x = 150 , y = 500)


def rollDicesController(root, dices):
    global countRoll
    global maintainNumber
    global maintain1
    global maintain2
    global maintain3
    global maintain4
    global maintain5
    if countRoll == 0:
        rollDices(dices,0)
    elif countRoll < 3:
        rollDices(dices,maintainNumber)
    else:
        print("Número maximo de lançadas atingido")
    imageList = createCanvas(dices, root)
    dicesCanvas(root, imageList)
    countRoll += 1
    maintain1 = False
    maintain2 = False
    maintain3 = False
    maintain4 = False
    maintain5 = False
    maintainNumber = 11111
    return

def dicesCanvas(root, imageList):
    if countRoll != 0:
        root.canvas.destroy()
    canvas = Canvas(root, width=300, height=200, bg="Green")
    root.canvas = canvas
    canvas.place(x = 400, y = 500)
    canvas.bind("<Button-1>", callback)
    x = 20

    for i in range(0, 5):
        canvas.create_image(x, 20, anchor = NW, image = imageList[i])
        x = x + 40


    # canvas.pack()

    # bc = Button(box, text = "Fechar", activeforeground = "yellow", activebackground = "pink", pady = 10)
    # bc.config(command = lambda: closeWindow(box))
    # bc.pack(padx=120, pady=30)
    # bc.pack(side = BOTTOM)

    root.update()
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
