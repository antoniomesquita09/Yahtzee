from .table import playersTable

__all__=[
            'ones',
            'twos',
            'threes',
            'fours',
            'fives',
            'sixes',
            'threeOfKind',
            'fourOfKind',
            'fullHouse',
            'smallSequence',
            'bigSequence',
            'yahtzee',
            'chance',
            'executePlaySup',
            'executePlayInf',
            'roundCounter',
        ]

countRounds = 1

# playersTable[player][sup/inf][indexPlay]

def pointsCounter():
    return playersTable

def roundCounter():
    global countRounds
    return countRounds

def executePlaySup(index, value):
    global countRounds


    if (playersTable[0][0][index] != ''):
        print('Jogada já executada!')
        return
    countRounds += 1
    playersTable[0][0][index] = value
    playersTable[0][0][7] += value
    return playersTable[0][0]

def executePlayInf(index, value):
    global countRounds
    
    if (playersTable[0][1][index] != ''):
        print('Jogada já executada!')
        return
    countRounds += 1
    playersTable[0][1][index] = value
    playersTable[0][1][8] += value
    return playersTable[0][1]

def countDices(dices, num):
    return dices.count(num)

def countEachDice(dices):
    eachDice = []
    eachDice.append(countDices(dices, 1))
    eachDice.append(countDices(dices, 2))
    eachDice.append(countDices(dices, 3))
    eachDice.append(countDices(dices, 4))
    eachDice.append(countDices(dices, 5))
    eachDice.append(countDices(dices, 6))
    return eachDice

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
    count = countEachDice(dices)

    if (count[0] >= 3):
        return sum(dices)
    if (count[1] >= 3):
        return sum(dices)
    if (count[2] >= 3):
        return sum(dices)
    if (count[3] >= 3):
        return sum(dices)
    if (count[4] >= 3):
        return sum(dices)
    if (count[5] >= 3):
        return sum(dices)
    return 0

def fourOfKind(dices):
    count = countEachDice(dices)

    if (count[0] >= 4):
        return sum(dices)
    if (count[1] >= 4):
        return sum(dices)
    if (count[2] >= 4):
        return sum(dices)
    if (count[3] >= 4):
        return sum(dices)
    if (count[4] >= 4):
        return sum(dices)
    if (count[5] >= 4):
        return sum(dices)
    return 0

def fullHouse(dices):
    count = countEachDice(dices)

    def checkRest(allDices, elem):
        rest = list(filter(lambda a: a != elem, allDices))
        if (equalDices(rest)):
            return 25
        return 0

    if(count[0] == 3):
        return checkRest(dices, 1)

    if(count[1] == 3):
        return checkRest(dices, 2)

    if(count[2] == 3):
        return checkRest(dices, 3)

    if(count[3] == 3):
        return checkRest(dices, 4)

    if(count[4] == 3):
        return checkRest(dices, 5)

    if(count[5] == 3):
        return checkRest(dices, 6)
    return 0

def smallSequence(dices):
    count = countEachDice(dices)

    if (
        count[0] >= 1 and
        count[1] >= 1 and
        count[2] >= 1 and
        count[3] >= 1
        ): return 30

    if (
        count[1] >= 1 and
        count[2] >= 1 and
        count[3] >= 1 and
        count[4] >= 1
        ): return 30

    if (
        count[2] >= 1 and
        count[3] >= 1 and
        count[4] >= 1 and
        count[5] >= 1
        ): return 30
    return 0

def bigSequence(dices):
    count = countEachDice(dices)

    if (
        count[0] == 1 and
        count[1] == 1 and
        count[2] == 1 and
        count[3] == 1 and
        count[4] == 1
        ): return 40

    if (
        count[1] == 1 and
        count[2] == 1 and
        count[3] == 1 and
        count[4] == 1 and
        count[5] == 1
        ): return 40
    return 0

def yahtzee(dices):
    if(equalDices(dices)):
        return 50
    return 0

def chance(dices):
    return sum(dices)
