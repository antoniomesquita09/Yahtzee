from tkinter import *

__all__=[
    'buildCanvas',
]

def destroyWindow(box):
    box.destroy()

def buildCanvas(root,img):
    #Criação de uma janela secundária
    box = Toplevel(root)
    box.title("Lançamento dos Dados")
    box.geometry("300x300")

    # Criação do canvas da janela secundária
    canvas = Canvas(box,width=300,height=200,bg="Pink")

    # Exibição das imagens no canvas
    x=20
    for i in range(0,6):
        canvas.create_image(x,20, anchor=NW, image=img[i])
        x=x+40

    canvas.pack()

    # Criação do botão de fechamento da janela secundária
    bc = Button(box, text = "Fechar",activeforeground = "yellow",activebackground = "pink",pady = 10)
    bc.config(command=lambda: destroyWindow(box))
    bc.pack(padx=120, pady=30)
    bc.pack(side = BOTTOM)

    # Redesenha a janela secundária para que as imagens sejam exibidas
    box.update()