from tkinter import Button, Label, Entry

from controllers.play import assignPlayers
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
    title = Label(root, text = "YAHTZEE", width = 50, anchor = "w")
    title.config(font=("Courier", 44))
    title.place(x = 200, y = 150)
    playersLabel(root)
    playersInput(root)
    finishButton = Button(root, text = "Iniciar partida", activeforeground = "yellow", activebackground = "pink", pady = 10, bg="green", fg="white" )
    finishButton.place(x = 300, y = 600)
    finishButton.config(command=lambda: handleClick())
    root.finishButton = finishButton
    root.title = title

    def handleClick():
        playersList = []

        countPlayers = 0

        if(root.inputOne.get() != ''):
            countPlayers += 1
            playersList.append(root.inputOne.get())
        if(root.inputTwo.get() != ''):
            countPlayers += 1
            playersList.append(root.inputTwo.get())
        if(root.inputThree.get() != ''):
            countPlayers += 1
            playersList.append(root.inputThree.get())
        if(root.inputFour.get() != ''):
            countPlayers += 1
            playersList.append(root.inputFour.get())
        if(root.inputFive.get() != ''):
            countPlayers += 1
            playersList.append(root.inputFive.get())
        if(root.inputSix.get() != ''):
            countPlayers += 1
            playersList.append(root.inputSix.get())
        
        if(countPlayers < 2):
            forbiddenInitialization = Label(root, text = "Mínimo de 2 jogadores para iniciar o jogo!", width = 50, anchor = "w", bg='red')
            forbiddenInitialization.place(x = 150, y = 500)
            root.forbiddenInitialization = forbiddenInitialization
            return

        playersList.sort()
        assignPlayers(playersList)
        destroyHome(root)
        rootDices(root, dices)
        rootPlay(root)
        return
    return

def destroyHome(root):
    try:
        root.forbiddenInitialization.destroy()
        root.title.destroy()
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
    except:
        print('Start game')
    return

def playersLabel(root):
    global players
    labelOne = Label(root, text = players[0], width = 12, anchor = "w")
    labelOne.place(x = 150,y = 290)
    labelTwo = Label(root, text = players[1], width = 12, anchor = "w")
    labelTwo.place(x = 150,y = 320)
    labelThree = Label(root, text = players[2], width = 12, anchor = "w")
    labelThree.place(x = 150,y = 350)
    labelFour = Label(root, text = players[3], width = 12, anchor = "w")
    labelFour.place(x = 150,y = 380)
    labelFive = Label(root, text = players[4], width = 12, anchor = "w")
    labelFive.place(x = 150,y = 410)
    labelSix = Label(root, text = players[5], width = 12, anchor = "w")
    labelSix.place(x = 150,y = 440)
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
    inputOne.place(x = 225, y = 290)
    inputTwo = Entry(root, width=50)
    inputTwo.place(x = 225, y = 320)
    inputThree = Entry(root, width=50)
    inputThree.place(x = 225, y = 350)
    inputFour = Entry(root, width=50)
    inputFour.place(x = 225, y = 380)
    inputFive = Entry(root, width=50)
    inputFive.place(x = 225, y = 410)
    inputSix = Entry(root, width=50)
    inputSix.place(x = 225, y = 440)
    root.inputOne = inputOne
    root.inputTwo = inputTwo
    root.inputThree = inputThree
    root.inputFour = inputFour
    root.inputFive = inputFive
    root.inputSix = inputSix
    return
