from ..pilha import *

__all__=[
            'ones',
            'twos',
            'threes',
            'fours',
            'fives',
            'sixes',
            'threeOfKind',
            'fourOfKind',
            'fullHouse'
        ]

def countDices(dices, num):
    return dices.count(num)

def equalDices(dices):
    return dices[1:] == dices[:-1]

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
        return sum(dices)
    if (countTwo >= 3):
        return sum(dices)
    if (countThree >= 3):
        return sum(dices)
    if (countFour >= 3):
        return sum(dices)
    if (countFive >= 3):
        return sum(dices)
    if (countSix >= 3):
        return sum(dices)
    return 0

def fourOfKind(dices):
    countOne = countDices(dices, 1)
    countTwo = countDices(dices, 2)
    countThree = countDices(dices, 3)
    countFour = countDices(dices, 4)
    countFive = countDices(dices, 5)
    countSix = countDices(dices, 6)

    if (countOne >= 4):
        return sum(dices)
    if (countTwo >= 4):
        return sum(dices)
    if (countThree >= 4):
        return sum(dices)
    if (countFour >= 4):
        return sum(dices)
    if (countFive >= 4):
        return sum(dices)
    if (countSix >= 4):
        return sum(dices)
    return 0

def fullHouse(dices):
    countOne = countDices(dices, 1)
    countTwo = countDices(dices, 2)
    countThree = countDices(dices, 3)
    countFour = countDices(dices, 4)
    countFive = countDices(dices, 5)
    countSix = countDices(dices, 6)

    def checkRest(allDices, elem):
        rest = list(filter(lambda a: a != elem, allDices))
        if (equalDices(rest)):
            return 25
        return 0

    if(countOne == 3):
        return checkRest(dices, 1)

    if(countTwo == 3):
        return checkRest(dices, 2)

    if(countThree == 3):
        return checkRest(dices, 3)

    if(countFour == 3):
        return checkRest(dices, 4)

    if(countFive == 3):
        return checkRest(dices, 5)

    if(countSix == 3):
        return checkRest(dices, 6)
    return 0
