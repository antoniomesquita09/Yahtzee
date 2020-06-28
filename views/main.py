from tkinter import Tk

from models.dices import initDices
from .dices import rootDices
from .play import rootPlay
from .newGame import rootNewGame

__all__=[
    'root',
]

def root():
    dices = initDices()

    root = Tk()
    root.geometry("800x800")
    root.title("Yahtzee")
    rootNewGame(root, dices)
    # rootDices(root, dices)
    # rootPlay(root)

    root.mainloop()
    return
