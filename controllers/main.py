from tkinter import IntVar, Checkbutton, Tk, Label, Listbox, SINGLE, BOTTOM, NW, Toplevel, Button, Canvas, PhotoImage

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
