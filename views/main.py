from tkinter import Tk

from models.dices import initDices
from .dices import rootDices
# from .table import rootTable

__all__=[
    'root',
]

def root():
    dices = initDices()

    root = Tk()
    root.geometry("800x800")
    root.title("Yahtzee")
    rootDices(root, dices)
    # rootTable(root)

    root.mainloop()
    return
