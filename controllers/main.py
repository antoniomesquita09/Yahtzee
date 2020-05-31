from tkinter import Tk

from models.dices.dices import initDices
from .dices import createLabel
from .play import rootPlay

__all__=[
    'root',
]

def root():

    dices = initDices()

    root = Tk()
    root.geometry("800x800")
    root.title("Jogo")
    createLabel(root, dices)
    rootPlay(root)

    root.mainloop()
    return
