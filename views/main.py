from tkinter import Tk

from models.dices import initDices
from .newGame import rootNewGame

__all__=[
    'root',
]

def root():
    dices = initDices()

    root = Tk()
    root.geometry("850x850")
    root.title("Yahtzee")
    rootNewGame(root, dices)

    root.mainloop()
    return
