from models.pilha import *
from models.rules.points import *
from models.rules.pointsTest import *
from models.dices.dices import *
from models.dices.dicesTest import *

dices = initDices()
rollDices(dices, 0)

# simular Full House

result = fullHouse(dices)
print("Dices: ", dices)
print("Points from a full House", result)

## TESTS
# Run unit tests from points

runPointsTests()

# Run unit tests from points

runDicesTests()

#    lambda a: a!=elem

# is equal as::::

#   def func(a):
#       return a !=elem
