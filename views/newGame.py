from tkinter import Button, Label, Entry

from views.dices import rootDices
from views.play import rootPlay

__all__=[
    'rootNewGame'
]

players = [
    'Jogador 1',
    'Jogador 2',
    'Jogador 3',
    'Jogador 4',
    'Jogador 5',
    'Jogador 6',
]

def rootNewGame(root, dices):
    playersLabel(root)
    playersInput(root)
    finishButton = Button(root, text = "Iniciar partida", activeforeground = "yellow", activebackground = "pink", pady = 50)
    finishButton.place(x = 400, y = 400)
    finishButton.config(command=lambda: handleClick())
    root.finishButton = finishButton

    def handleClick():
        test = []

        if(root.inputOne.get() != ''):
            test.append(root.inputOne.get())
        if(root.inputTwo.get() != ''):
            test.append(root.inputTwo.get())
        if(root.inputThree.get() != ''):
            test.append(root.inputThree.get())
        if(root.inputFour.get() != ''):
            test.append(root.inputFour.get())
        if(root.inputFive.get() != ''):
            test.append(root.inputFive.get())
        if(root.inputSix.get() != ''):
            test.append(root.inputSix.get())

        x = sorted(test)
        print(x)
        destroyHome(root)
        rootDices(root, dices)
        rootPlay(root)
        return
    return

def destroyHome(root):
    root.labelOne.destroy()
    root.labelTwo.destroy()
    root.labelThree.destroy()
    root.labelFour.destroy()
    root.labelFive.destroy()
    root.labelSix.destroy()
    root.inputOne.destroy()
    root.inputTwo.destroy()
    root.inputThree.destroy()
    root.inputFour.destroy()
    root.inputFive.destroy()
    root.inputSix.destroy()
    root.finishButton.destroy()
    return

def playersLabel(root):
    global players
    labelOne = Label(root, text = players[0], width = 12, anchor = "w")
    labelOne.place(x = 10,y = 90)
    labelTwo = Label(root, text = players[1], width = 12, anchor = "w")
    labelTwo.place(x = 10,y = 110)
    labelThree = Label(root, text = players[2], width = 12, anchor = "w")
    labelThree.place(x = 10,y = 130)
    labelFour = Label(root, text = players[3], width = 12, anchor = "w")
    labelFour.place(x = 10,y = 150)
    labelFive = Label(root, text = players[4], width = 12, anchor = "w")
    labelFive.place(x = 10,y = 170)
    labelSix = Label(root, text = players[5], width = 12, anchor = "w")
    labelSix.place(x = 10,y = 190)
    root.labelOne = labelOne
    root.labelTwo = labelTwo
    root.labelThree = labelThree
    root.labelFour = labelFour
    root.labelFive = labelFive
    root.labelSix = labelSix
    return

def playersInput(root):
    global players
    inputOne = Entry(root, width=50)
    inputOne.place(x = 75, y = 90)
    inputTwo = Entry(root, width=50)
    inputTwo.place(x = 75, y = 110)
    inputThree = Entry(root, width=50)
    inputThree.place(x = 75, y = 130)
    inputFour = Entry(root, width=50)
    inputFour.place(x = 75, y = 150)
    inputFive = Entry(root, width=50)
    inputFive.place(x = 75, y = 170)
    inputSix = Entry(root, width=50)
    inputSix.place(x = 75, y = 190)
    root.inputOne = inputOne
    root.inputTwo = inputTwo
    root.inputThree = inputThree
    root.inputFour = inputFour
    root.inputFive = inputFive
    root.inputSix = inputSix
    return
