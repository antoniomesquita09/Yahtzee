from tkinter import Tk

from models.dices import initDices
from .dices import rootDices
from .play import rootPlay

__all__=[
    'root',
]

def root():
    dices = initDices()

    root = Tk()
    root.geometry("800x800")
    root.title("Yahtzee")
    rootDices(root, dices)
    rootPlay(root)

    root.mainloop()
    return
