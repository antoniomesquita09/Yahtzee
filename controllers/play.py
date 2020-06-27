from models.points import ones, twos, threes, fours, fives, sixes, threeOfKind, fourOfKind, fullHouse, smallSequence, bigSequence,  yahtzee, chance

from models.points import executePlaySup, executePlayInf

__all__=[
    'executePlay',
]

def executePlay(playList, dices, player):
    try:
        index = (playList.curselection())[0]
        result = 0
        if(index == 0):
            result = ones(dices)
            return executePlaySup(0, result, player)
        elif(index == 1):
            result = twos(dices)
            return executePlaySup(1, result, player)
        elif(index == 2):
            result = threes(dices)
            return executePlaySup(2, result, player)
        elif(index == 3):
            result = fours(dices)
            return executePlaySup(3, result, player)
        elif(index == 4):
            result = fives(dices)
            return executePlaySup(4, result, player)
        elif(index == 5):
            result = sixes(dices)
            return executePlaySup(5, result, player)
        elif(index == 6):
            result = threeOfKind(dices)
            return executePlayInf(0, result, player)
        elif(index == 7):
            result = fourOfKind(dices)
            return executePlayInf(1, result, player)
        elif(index == 8):
            result = fullHouse(dices)
            return executePlayInf(2, result, player)
        elif(index == 9):
            result = smallSequence(dices)
            return executePlayInf(3, result, player)
        elif(index == 10):
            result = bigSequence(dices)
            return executePlayInf(4, result, player)
        elif(index == 11):
            result = yahtzee(dices)
            return executePlayInf(5, result, player)
        elif(index == 12):
            result = chance(dices)
            return executePlayInf(6, result, player)
        else:
            return
        return
    except:
        print("you must enter a play")
        return
