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
    assert sixes(dices) == 0

def testThreeOfKind(dices):
    assert threeOfKind(dices) == 0

def testFourOfKind(dices):
    assert fourOfKind(dices) == 0

def testFullHouse(dices):
    assert fullHouse(dices) == 0

testDices = [1, 2, 3, 4, 5]

def runTests():
    testOnes(testDices)
    testTwos(testDices)
    testThrees(testDices)
    testFours(testDices)
    testFives(testDices)
    testSixes(testDices)
    testThreeOfKind(testDices)
    testFourOfKind(testDices)
    testFullHouse(testDices)
    print('========> Tests passed successfully! <=========')
    return
