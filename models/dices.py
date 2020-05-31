
import random

__all__=[
    'rollDices',
    'initDices'
]

def initDices():
    init = [0, 0, 0, 0, 0]
    return init

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
