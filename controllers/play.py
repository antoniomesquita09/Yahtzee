from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

from models.dices.dices import rollDices
from models.rules.points import ones, twos, threes, fours, fives, sixes, threeOfKind, fourOfKind, fullHouse, smallSequence, bigSequence,  yahtzee, chance

__all__=[
    'executePlay',
]

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
