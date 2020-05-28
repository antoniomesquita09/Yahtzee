from tkinter import *

from models.pilha import *
from models.rules.points import *
from models.rules.pointsTest import *
from models.dices.dices import *
from models.dices.dicesTest import *
from controllers.main import *

dices = initDices()
rollDices(dices, 0)

# simular Full House

result = fullHouse(dices)
print("Dices: ", dices)
print("Points from a full House", result)

## TESTS
# Run unit tests from points

runPointsTests()

# Run unit tests from points

runDicesTests()

# Build Canvas

def criaCanvas(root):
    canvas = Canvas(root,width=300,height=300,bg="Pink")
    canvas.pack()
    canvas.create_image(20,20, anchor=NW, image=img)

# Create main window
root = Tk()
root.geometry("400x400")
root.title("Jogo")

# Roll dices button
b1 = Button(root, text = "Lancar Dados",activeforeground = "yellow",activebackground = "pink",pady = 10)
b1.config(command=lambda: buildCanvas(root,img))
b1.pack(padx=120, pady=30)
b1.pack(side = BOTTOM)

# Load images in a list
img = []
img.append(PhotoImage(file="dado_1.png"))
img.append(PhotoImage(file="dado_2.png"))
img.append(PhotoImage(file="dado_3.png"))
img.append(PhotoImage(file="dado_4.png"))
img.append(PhotoImage(file="dado_5.png"))
img.append(PhotoImage(file="dado_6.png"))

root.mainloop()
