import random

from models.pilha import *
from models.points import *
from models.pointsTest import *

# simular dados

lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))

# lista de dados

# dices = retList()

# run unit tests from points

runTests()

# testa uma jogada em trinca

# result = threeOfKind(dices)
dices = [1,2,1,2,1]
result = fullHouse(dices)

print('fulhouse points:: ', result)

