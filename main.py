from pilha import *

pilha_push([3.0,3.0])
pilha_push([2.0,2.0])
pilha_push([1.0,1.0])

while not pilha_vazia():
    e=pilha_pop()
    print("(%.1f,%.1f)"%(e[0],e[1]))



# tests =======>

# lst_insIni(0)
# lst_insFin(2)
# lst_insFin(3)
# lst_insFin(4)

# exibe()

# lst_retIni()
# lst_retFin()

# exibe()

# lst_posIni()

# lst_prox()

# exibe()

# result = pilha_vazia()
# pilha_push(4)
# exibe()

# result = pilha_pop()
# print(result)
# lst_vazia()
