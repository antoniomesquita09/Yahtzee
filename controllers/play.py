from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from models.dices.dices import rollDices
from models.rules.points import ones, twos, threes, fours, fives, sixes, threeOfKind, fourOfKind, fullHouse, smallSequence, bigSequence,  yahtzee, chance

__all__=[
    'rootPlay',
]

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

def executePlay(playList, dices):
    try:
        index = (playList.curselection())[0]
        result = 0
        if(index == 0):
            result = ones(dices)
        elif(index == 1):
            result = twos(dices)
        elif(index == 2):
            result = threes(dices)
        elif(index == 3):
            result = fours(dices)
        elif(index == 4):
            result = fives(dices)
        elif(index == 5):
            result = sixes(dices)
        elif(index == 6):
            result = threeOfKind(dices)
        elif(index == 7):
            result = fourOfKind(dices)
        elif(index == 8):
            result = fullHouse(dices)
        elif(index == 9):
            result = smallSequence(dices)
        elif(index == 10):
            result = bigSequence(dices)
        elif(index == 11):
            result = yahtzee(dices)
        elif(index == 12):
            result = chance(dices)
        else:
            return
        print(result)
        return
    except:
        print("you must enter a play")
        return

def rootPlay(root, dices):
    playOptions(root, dices)
    return
