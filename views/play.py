from tkinter import Button

from models.points import pointsCounter

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
        playersTable = pointsCounter()
        file = open('file.txt','w')

        for player in playersTable:
            writeFile(player[0], file) # plays sup
            writeFile(player[1], file) # plays inf
        return
    return

def rootPlay(root):
    finishButton(root)
    return
