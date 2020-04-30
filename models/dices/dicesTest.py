from dices import *

__all__=[
    'runTests',
]


def testRodaDados(dices):
    test = dices[0:5]
    rodaDados(test,11111)
    assert test == dices
    rodaDados(test,11110)
    assert test[0:4] == dices[0:4]
    rodaDados(test,11100)
    assert test[0:3] == dices[0:3]
    rodaDados(test,11000)
    assert test[0:2] == dices[0:2]
    rodaDados(test,10000)
    assert test[0] == dices[0]
    test = dices[0:5]
    rodaDados(test,1111)
    assert test[1:5] == dices[1:5]
    rodaDados(test,111)
    assert test[2:5] == dices[2:5]
    rodaDados(test,11)
    assert test[3:5] == dices[3:5]
    rodaDados(test,1)
    assert test[4] == dices[4]

testDices = [1, 2, 3, 4, 5]

def runTests():
    testRodaDados(testDices)
    print('========> Tests passed successfully! <=========')
    return True

runTests()
