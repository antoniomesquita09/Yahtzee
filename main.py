import random

from models.pilha import *
from models.points import *


lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))
lst_insFin(random.randint(1,6))

dices = retList()

result = threeOfKind(dices)

print('Trinca:', result)
