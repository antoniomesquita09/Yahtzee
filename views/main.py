from tkinter import Tk

from models.dices import initDices
from .dices import rootDices

__all__=[
    'root',
]

def root():
    dices = initDices()

    root = Tk()
    root.geometry("800x800")
    root.title("Yahtzee")
    rootDices(root, dices)

    root.mainloop()
    return
