
from models.table import resumePlayersTable
from views.dices import resumePlayer
from models.points import resumeRound

def resumeGame(file):
    resumedGame = open(file, 'r')

    firstLine = resumedGame.readline()
    currentInfo = firstLine.split(' ')
    currentPlayer = currentInfo[0]
    currentRound = currentInfo[1]
    resumePlayer(int(currentPlayer))
    resumeRound(int(currentRound))

    players = resumedGame.readline()
    playersArray = players.split(' ')
    playersArray.remove('\n')
    # rounds = resumedGame.readline()
    recomposedTable = []
    auxArray = []
    aux = 0
    for line in resumedGame:
        aux += 1
        lineArray = line.split(' ')
        lineArray.remove('\n')
        for i in range(0, len(lineArray)):
            if (lineArray[i] == 'empty'):
                lineArray[i] = ''
            else:
                lineArray[i] = int(lineArray[i])
        if (aux % 2 == 0):
            auxArray.append(lineArray)
            recomposedTable.append(auxArray)
            auxArray = []
        else:
            auxArray.append(lineArray)
    resumePlayersTable(recomposedTable)
    return playersArray
