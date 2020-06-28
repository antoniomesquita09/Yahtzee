from tkinter import Button, filedialog

from controllers.play import getPlayersName
from models.points import pointsCounter, roundCounter
from views.dices import currentPlayer

__all__=[
    'rootPlay',
]

def play(root):
    return

    
def writeFile(array, file):
    for elem in array:
        if(elem == 0):
            file.write('0 ')
        elif(elem == ''):
            file.write('empty ')
        else:
            file.write(str(elem) + ' ')
    file.write('\n')
    return

def finishButton(root):
    finishButton = Button(root, text = "Terminar partida", activeforeground = "yellow", activebackground = "pink", pady = 10)
    finishButton.place(x = 150, y = 730)
    finishButton.config(command=lambda: handleClick())

    def handleClick():
        file = filedialog.asksaveasfile(mode='w', filetypes = (("txt files","*.txt"),("all files","*.*")), defaultextension=".txt", title="Salvar andamento")

        if file is None:
            return

        playersTable = pointsCounter()
        playersName = getPlayersName()

        current = currentPlayer()
        currentRound = roundCounter()

        file.write(str(current) + ' ' + str(currentRound))
        file.write('\n')

        for person in playersName:
            file.write(person + ' ')
        
        file.write('\n')

        for player in playersTable:
            writeFile(player[0], file) # plays sup
            writeFile(player[1], file) # plays inf

        return root.destroy()
    return

def rootPlay(root):
    finishButton(root)
    return
