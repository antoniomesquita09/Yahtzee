

__all__=[
    'resumePlayersTable',
    'getPlayersTable',
    'getWinner'
]

winner = 0

playersTable = [
    # first player
    [
        [
            '',  # ones
            '',  # twos
            '',  # threes
            '',  # fours
            '',  # fives
            '',  # sixes
            '',  # bonus
            0,  # total
        ],
        [
            '', # tripple
            '', # four
            '', # fullhouse
            '', # small
            '', # big
            '', # yahtzee
            '', # chance
            '', # bonus
            0, # total
        ]
    ],
    # second player
    [
        [
            '',  # ones
            '',  # twos
            '',  # threes
            '',  # fours
            '',  # fives
            '',  # sixes
            '',  # bonus
            0,  # total
        ],
        [
            '', # tripple
            '', # four
            '', # fullhouse
            '', # small
            '', # big
            '', # yahtzee
            '', # chance
            '', # bonus
            0, # total
        ]
    ],
    # third player
    [
        [
            '',  # ones
            '',  # twos
            '',  # threes
            '',  # fours
            '',  # fives
            '',  # sixes
            '',  # bonus
            0,  # total
        ],
        [
            '', # tripple
            '', # four
            '', # fullhouse
            '', # small
            '', # big
            '', # yahtzee
            '', # chance
            '', # bonus
            0, # total
        ]
    ],
    # fourth player
    [
        [
            '',  # ones
            '',  # twos
            '',  # threes
            '',  # fours
            '',  # fives
            '',  # sixes
            '',  # bonus
            0,  # total
        ],
        [
            '', # tripple
            '', # four
            '', # fullhouse
            '', # small
            '', # big
            '', # yahtzee
            '', # chance
            '', # bonus
            0, # total
        ]
    ],
    # fifth player
    [
        [
            '',  # ones
            '',  # twos
            '',  # threes
            '',  # fours
            '',  # fives
            '',  # sixes
            '',  # bonus
            0,  # total
        ],
        [
            '', # tripple
            '', # four
            '', # fullhouse
            '', # small
            '', # big
            '', # yahtzee
            '', # chance
            '', # bonus
            0, # total
        ]
    ],
    # sixth player
    [
        [
            '',  # ones
            '',  # twos
            '',  # threes
            '',  # fours
            '',  # fives
            '',  # sixes
            '',  # bonus
            0,  # total
        ],
        [
            '', # tripple
            '', # four
            '', # fullhouse
            '', # small
            '', # big
            '', # yahtzee
            '', # chance
            '', # bonus
            0, # total
        ]
    ]
]


def resumePlayersTable(resumedGame):
    global playersTable
    playersTable = resumedGame
    return playersTable

def getPlayersTable():
    global playersTable
    return playersTable


def checkWinner():
    global winner
    tot = 0
    for i in range(0, len(playersTable)):
        totalSup = playersTable[i][0][7]
        totalInf = playersTable[i][1][8]
        total = int(totalSup) + int(totalInf)
        if(total > tot):
            tot = total
            winner = i
    
def getWinner():
    global winner
    return winner
