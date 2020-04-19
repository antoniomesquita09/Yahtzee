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
    supposedToPass = [1,2,1,1,1]
    assert threeOfKind(supposedToPass) == sum(supposedToPass)
    assert threeOfKind(dices) == 0

def testFourOfKind(dices):
    supposedToPass = [1,2,1,1,1]
    assert fourOfKind(supposedToPass) == sum(supposedToPass)
    assert fourOfKind(dices) == 0

def testFullHouse(dices):
    supposedToPass = [1,2,1,2,2]
    assert fullHouse(supposedToPass) == 25
    assert fullHouse(dices) == 0

def testSmallSequence(dices):
    supposedToFail = [1,1,1,2,4]
    assert smallSequence(supposedToFail) == 0
    assert smallSequence(dices) == 30

def testBigSequence(dices):
    supposedToFail = [1,1,1,2,4]
    assert bigSequence(supposedToFail) == 0
    assert bigSequence(dices) == 40

def testYahtzee(dices):
    assert yahtzee(dices) == 0

def testChance(dices):
    assert chance(dices) == 15

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
    testSmallSequence(testDices)
    testBigSequence(testDices)
    testYahtzee(testDices)
    testChance(testDices)
    print('========> Tests passed successfully! <=========')
    return True
