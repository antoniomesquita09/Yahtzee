from pilha import *

__all__=[
            'ones',
            'twos',
            'threes',
            'fours',
            'fives',
            'sixes',
            'threeOfKind'
        ]

def countDices(dices, num):
    return dices.count(num)

def sumDices():
    if lst_vazia() == True:
        return 0
    value = lst_retIni()
    return sumDices() + value

def ones(dices):
    count = countDices(dices, 1)
    return count

def twos(dices):
    count = countDices(dices, 2)
    return count * 2

def threes(dices):
    count = countDices(dices, 3)
    return count * 3

def fours(dices):
    count = countDices(dices, 4)
    return count * 4

def fives(dices):
    count = countDices(dices, 5)
    return count * 5

def sixes(dices):
    count = countDices(dices, 6)
    return count * 6

def threeOfKind(dices):
    countOne = countDices(dices, 1)
    countTwo = countDices(dices, 2)
    countThree = countDices(dices, 3)
    countFour = countDices(dices, 4)
    countFive = countDices(dices, 5)
    countSix = countDices(dices, 6)

    if (countOne >= 3):
        return sumDices()
    if (countTwo >= 3):
        return sumDices()
    if (countThree >= 3):
        return sumDices()
    if (countFour >= 3):
        return sumDices()
    if (countFive >= 3):
        return sumDices()
    if (countSix >= 3):
        return sumDices()
    return 0
