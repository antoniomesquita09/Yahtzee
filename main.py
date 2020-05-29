from models.pilha import *
from models.rules.points import *
from models.rules.pointsTest import *
from models.dices.dices import *
from models.dices.dicesTest import *
from controllers.main import root

## TESTS
# Run unit tests from points

runPointsTests()

# Run unit tests from points

runDicesTests()

# Run canvas

root()
