import random

from models.pilha import *
from models.points import *

# simular dados

lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))

# lista de dados

dices = retList()

# testa uma jogada em trinca

result = threeOfKind(dices)

print('Trinca:', result)
