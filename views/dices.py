from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage, StringVar

from controllers.play import executePlay
from controllers.dices import rollDicesController, canvasClick, resetCountRoll
from models.points import roundCounter

__all__=[
    'rootDices',
]

valuesSup = [
    'ones',
    'twos',
    'three',
    'fours',
    'fives',
    'sixes',
    'bonus',
    'total',
]

valuesInf = [
    'Trinca',
    'Quadra',
    'Full House',
    'Sequência Menor',
    'Sequência Maior',
    'Yahtzee',
    'Chance',
    'Bonus',
    'total',
]

numPlayer = 6
player = 0


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
    buttonPlay.config(command=lambda: handleClick(playList, dices))
    buttonPlay.place(x = 150 , y = 400)

    for i in range(0, len(valuesSup)):
        value = valuesSup[i]
        valueLabel = value + 'Lable'
        valueLabel = Label(root, text = value)
        valueLabel.place(x = 350, y = i*50 + 10)

    for i in range(0, len(valuesInf)):
        value = valuesInf[i]
        valueLabel = value + 'Lable'
        valueLabel = Label(root, text = value)
        valueLabel.place(x = 550, y = i*50 + 10)

    def handleClick(playList, dices):
        global player
        array = executePlay(playList, dices, player)

        if (array == None):
            forbiddenPlay = Label(root, text = "Execute uma jogada válida!", width = 25, anchor = "w", bg='red')
            forbiddenPlay.place(x = 80, y = 360)
            root.forbiddenPlay = forbiddenPlay
            return

        xPostion = 450
        listLabel = valuesSup
        if (len(array) == 9):
            xPostion = 700
            listLabel = valuesInf

        for i in range(0, len(array)):
            value = listLabel[i]
            value = StringVar()
            value.set(array[i])
            valueLabel = listLabel[i] + 'Lable'
            valueLabel = Label(root, textvariable=value, width="10")
            valueLabel.place(x = xPostion, y = i*50 + 10)

        try:
            if (root.forbiddenRoll):
                root.forbiddenRoll.destroy()
        except:
            print('Lançamento de dado permitido')

        try:
            if (root.forbiddenPlay):
                root.forbiddenPlay.destroy()
        except:
            print('Jogada permitida')

        nextPlayer()
        handlePlayer(root, player)
        rollCounter = resetCountRoll()
        handleCount(root, rollCounter)
        root.canvas.destroy()
        return
    return

def nextPlayer():
    global player, numPlayer
    if (player == numPlayer -1):
        player = 0
        return
    player += 1
    return

def rollDicesButton(root, dices):
    b1 = Button(root, text = "Lancar Dados", activeforeground = "yellow", activebackground = "pink", pady = 10)
    b1.config(command=lambda: handleClick(root, dices))

    countPlayLabel = Label(root, text = "Jogadas:", width = 50, anchor = "w")
    countPlayLabel.place(x = 10, y = 600)
    
    countRoundLabel = Label(root, text = "Round:", width = 50, anchor = "w")
    countRoundLabel.place(x = 10, y = 650)
    
    playerLabel = Label(root, text = "Jogador:", width = 7, anchor = "w")
    playerLabel.place(x = 500, y = 750)

    def handleClick(root, dices):
        # global countRoll, countRounds
        rollCounter = rollDicesController(root, dices)
        roundsCounter = roundCounter()
        
        handleCount(root, rollCounter)
        handleRound(root, roundsCounter)
        return

    b1.pack(padx=120, pady=30)
    b1.pack(side = BOTTOM)
    b1.place(x = 150 , y = 500)
    return

def handlePlayer(root, player):
    playerVariable = StringVar()
    playerVariable.set(player + 1) # sum to player index
    playerLabel = Label(root, textvariable=playerVariable)
    playerLabel.place(x = 600, y = 750)
    root.playerLabel = playerLabel
    return

def handleCount(root, rollCounter):
    countRollVariable = StringVar()
    countRollVariable.set(rollCounter)
    countRollLabel = Label(root, textvariable=countRollVariable)
    countRollLabel.place(x = 150, y = 600)
    root.countRollLabel = countRollLabel
    return

def handleRound(root, roundsCounter):
    countRoundsVariable = StringVar()
    countRoundsVariable.set(roundsCounter)
    countRoundsLabel = Label(root, textvariable=countRoundsVariable)
    countRoundsLabel.place(x = 150, y = 650)
    root.countRoundsLabel = countRoundsLabel
    return


def rootDices(root, dices):
    global player
    handlePlayer(root, player)
    playOptions(root, dices)
    rollDicesButton(root, dices)
    return
