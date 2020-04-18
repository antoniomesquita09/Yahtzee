from points import *

__all__=[
    'runTests',
]

def testOnes(dices):
    assert ones(dices) == 1

def testTwos(dices):
    assert twos(dices) == 2

def testThrees(dices):
    assert threes(dices) == 3

def testFours(dices):
    assert fours(dices) == 4

def testFives(dices):
    assert fives(dices) == 5

def testSixes(dices):
    assert sixes(dices) == 6

def testThreeOfKind(dices):
    assert threeOfKind(dices) == 0

randDices = [1, 2, 3, 4, 5, 6]

def runTests():
    testOnes(randDices)
    testTwos(randDices)
    testThrees(randDices)
    testFours(randDices)
    testFives(randDices)
    testSixes(randDices)
    testThreeOfKind(randDices)
    print('Tests passed successfully!')
    return
