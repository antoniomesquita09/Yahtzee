from tkinter import Tk

from models.dices.dices import initDices
from .dices import createLabel

__all__=[
    'root',
]

def root():

    dices = initDices()

    root = Tk()
    root.geometry("400x400")
    root.title("Jogo")
    createLabel(root, dices)

    root.mainloop()
    return
