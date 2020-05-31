from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from models.dices.dices import rollDices

__all__=[
    'rootPlay',
]

def playLeft(root):
    ones = Label(root, text = "Um", width = 12, anchor = "w")
    ones.place(x =210, y = 10)
    test1 = IntVar()
    play1 =  Checkbutton(root, text="manter", variable = test1)
    play1.place(x = 275, y = 10)

    twos = Label(root, text = "Dois", width = 12, anchor = "w")
    twos.place(x =210, y = 50)
    test2 = IntVar()
    play2 =  Checkbutton(root, text="manter", variable = test2)
    play2.place(x = 275, y = 50)

    threes = Label(root, text = "Três", width = 12, anchor = "w")
    threes.place(x =210, y = 90)
    test3 = IntVar()
    play3 =  Checkbutton(root, text="manter", variable = test3)
    play3.place(x = 275, y = 90)

    fours = Label(root, text = "Quatro", width = 12, anchor = "w")
    fours.place(x =210, y = 130)
    test4 = IntVar()
    play4 =  Checkbutton(root, text="manter", variable = test4)
    play4.place(x = 275, y = 130)

    fives = Label(root, text = "Cinco", width = 12, anchor = "w")
    fives.place(x =210, y = 170)
    test5 = IntVar()
    play5 =  Checkbutton(root, text="manter", variable = test5)
    play5.place(x = 275, y = 170)

    sixes = Label(root, text = "Seis", width = 12, anchor = "w")
    sixes.place(x =210, y = 210)
    test6 = IntVar()
    play6 =  Checkbutton(root, text="manter", variable = test6)
    play6.place(x = 275, y = 210)

    return

def playRight(root):
    ones = Label(root, text = "Trinca", width = 20, anchor = "w")
    ones.place(x =410, y = 10)
    test1 = IntVar()
    play1 =  Checkbutton(root, text="manter", variable = test1)
    play1.place(x = 550, y = 10)

    twos = Label(root, text = "Quadra", width = 20, anchor = "w")
    twos.place(x =410, y = 50)
    test2 = IntVar()
    play2 =  Checkbutton(root, text="manter", variable = test2)
    play2.place(x = 550, y = 50)

    threes = Label(root, text = "Full house", width = 20, anchor = "w")
    threes.place(x =410, y = 90)
    test3 = IntVar()
    play3 =  Checkbutton(root, text = "manter", variable = test3)
    play3.place(x = 550, y = 90)

    fours = Label(root, text = "Sequência Mínima", width = 20, anchor = "w")
    fours.place(x =410, y = 130)
    test4 = IntVar()
    play4 =  Checkbutton(root, text="manter", variable = test4)
    play4.place(x = 550, y = 130)

    fives = Label(root, text = "Sequência Máxima", width = 20, anchor = "w")
    fives.place(x =410, y = 170)
    test5 = IntVar()
    play5 =  Checkbutton(root, text="manter", variable = test5)
    play5.place(x = 550, y = 170)

    sixes = Label(root, text = "Yahtzee", width = 20, anchor = "w")
    sixes.place(x =410, y = 210)
    test6 = IntVar()
    play6 =  Checkbutton(root, text="manter", variable = test6)
    play6.place(x = 550, y = 210)

    seven = Label(root, text = "Chance", width = 20, anchor = "w")
    seven.place(x =410, y = 250)
    test7 = IntVar()
    play7 =  Checkbutton(root, text="manter", variable = test7)
    play7.place(x = 550, y = 250)

    return

def rootPlay(root):
    playLeft(root)
    playRight(root)
    return

    # lbDado2 = Label(root, text = "yahtzee", width = 20, anchor = "w")
    # lbDado2.place(x = 10,y = 50)
    # maintain2 = IntVar()
    # c2 =  Checkbutton(root, text="manter", variable = maintain2)
    # c2.place(x = 75 ,y = 50)

    # lbDado3 = Label(root, text = "yahtzee", width = 12, anchor = "w")
    # lbDado3.place(x = 10, y = 90)
    # maintain3 = IntVar()
    # c3 =  Checkbutton(root, text="manter", variable = maintain3)
    # c3.place(x = 75 ,y = 90)

    # lbDado4 = Label(root, text = "yahtzee", width = 12, anchor = "w")
    # lbDado4.place(x = 10, y = 130)
    # maintain4 = IntVar()
    # c4 =  Checkbutton(root, text="manter", variable = maintain4)
    # c4.place(x = 75 ,y = 130)

    # lbDado5 = Label(root, text = "yahtzee", width = 12, anchor = "w")
    # lbDado5.place(x = 10, y = 170)
    # maintain5 = IntVar()
    # c5 =  Checkbutton(root, text="manter", variable = maintain5)
    # c5.place(x = 75 ,y = 170)

    # b1 = Button(root, text = "Lancar Dados", activeforeground = "yellow", activebackground = "pink", pady = 10)
    # b1.config(command=lambda: rollDicesController( root, dices, maintain5.get(), maintain4.get(), maintain3.get(), maintain2.get(), maintain1.get()))
    # b1.pack(padx=120, pady=30)
    # b1.pack(side = BOTTOM)
    # b1.place(x = 25 , y = 300)
