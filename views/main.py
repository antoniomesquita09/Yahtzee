from tkinter import Tk

from models.dices.dices import initDices
from .dices import rootDices

__all__=[
    'root',
]

def root():
    dices = initDices()

    root = Tk()
    root.geometry("800x800")
    root.title("Jogo")
    rootDices(root, dices)

    root.mainloop()
    return
