
import random

__all__=[
    'rollDices',
    'initDices',
    'restartDices'
]

dices = []

def initDices():
    global dices
    dices.append(0)
    dices.append(0)
    dices.append(0)
    dices.append(0)
    dices.append(0)
    return dices

def restartDices():
    global dices
    dices[0] = 0
    dices[1] = 0
    dices[2] = 0
    dices[3] = 0
    dices[4] = 0
    return dices

def rollDices(dices, dadosFixos):
    if dadosFixos >= 10000:
        dadosFixos = dadosFixos - 10000
    else:
        dices[0] = random.randint(1,6)

    if dadosFixos >= 1000:
        dadosFixos = dadosFixos - 1000
    else:
        dices[1] = random.randint(1,6)

    if dadosFixos >= 100:
        dadosFixos = dadosFixos - 100
    else:
        dices[2] = random.randint(1,6)

    if dadosFixos >= 10:
        dadosFixos = dadosFixos - 10
    else:
        dices[3] = random.randint(1,6)

    if dadosFixos >= 1:
        dadosFixos = dadosFixos - 1
    else:
        dices[4] = random.randint(1,6)
    return dices
