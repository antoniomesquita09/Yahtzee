from ..dices import rollDices, initDices

__all__=[
    'runDicesTests',
]


def testRollDices(dices):
    test = dices[0:5]
    rollDices(test,11111)
    assert test == dices
    rollDices(test,11110)
    assert test[0:4] == dices[0:4]
    rollDices(test,11100)
    assert test[0:3] == dices[0:3]
    rollDices(test,11000)
    assert test[0:2] == dices[0:2]
    rollDices(test,10000)
    assert test[0] == dices[0]
    test = dices[0:5]
    rollDices(test,1111)
    assert test[1:5] == dices[1:5]
    rollDices(test,111)
    assert test[2:5] == dices[2:5]
    rollDices(test,11)
    assert test[3:5] == dices[3:5]
    rollDices(test,1)
    assert test[4] == dices[4]

# def testInitDices():
    # test = initDices()
    # assert test == [0, 0, 0, 0, 0]

testDices = [1, 2, 3, 4, 5]

def runDicesTests():
    # testInitDices()
    testRollDices(testDices)
    print('========> Dices tests passed successfully! <=========')
    return True
