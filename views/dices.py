from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from controllers.play import executePlay
from controllers.dices import rollDicesController, canvasClick

__all__=[
    'rootDices',
]

countRoll = 0

def playOptions(root, dices):
    playLabel = Label(root, text = "Executar jogada:", width = 50, anchor = "w")
    playLabel.place(x = 10, y = 10)
    playList = Listbox(root, width = 20, height = 20 , selectmode = SINGLE)
    playList.insert(1 ,"Um")
    playList.insert(2, "Dois")
    playList.insert(3, "Três")
    playList.insert(4, "Quatro")
    playList.insert(5, "Cinco")
    playList.insert(6, "Seis")
    playList.insert(7, "Trinca")
    playList.insert(8, "Quadra")
    playList.insert(9, "Full house")
    playList.insert(10, "Sequência Mínima")
    playList.insert(11, "Sequência Máxima")
    playList.insert(12, "Yahtzee")
    playList.insert(13, "Chance")
    playList.place(x = 150, y = 10)

    buttonPlay = Button(root, text = "Executar Jogada", activeforeground = "yellow", activebackground = "pink", pady = 10)
    buttonPlay.config(command=lambda: executePlay(playList, dices))
    buttonPlay.place(x = 150 , y = 400)
    return

def rollDicesButton(root, dices):
    b1 = Button(root, text = "Lancar Dados", activeforeground = "yellow", activebackground = "pink", pady = 10)
    b1.config(command=lambda: handleClick(root, dices))

    def handleClick(root, dices):
        global countRoll
        countRoll = rollDicesController( root, dices)
        print(countRoll)
        return

    b1.pack(padx=120, pady=30)
    b1.pack(side = BOTTOM)
    b1.place(x = 150 , y = 500)


def rootDices(root, dices):
    playOptions(root, dices)
    rollDicesButton(root, dices)
    return
