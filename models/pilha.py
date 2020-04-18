__all__=[
            'retList',
            'lst_vazia',
            'lst_insIni',
            'lst_insFin',
            'lst_retIni',
            'lst_retFin',
            'lst_posIni',
            'lst_prox',
            'pilha_vazia',
            'pilha_push',
            'pilha_pop',
        ]

def lst_vazia():
    if myList==[]:
        return True
    return False

def lst_insIni(elem):
    myList.insert(-1, elem)
    return

def lst_insFin(elem):
    myList.append(elem)
    return

def lst_retIni():
    if lst_vazia() == True:
        return None
    return myList.pop(0)

def lst_retFin():
    if lst_vazia() == True:
        return None
    return myList.pop(-1)

def lst_posIni():
    if lst_vazia() == True:
        return myList.append(None)
    current = myList.pop(0)
    return myList.append(current)

def lst_prox():
    if lst_vazia() == True:
        return myList.append(None)
    current = myList.pop(0)
    myList.insert(1, current)
    return current

def pilha_vazia():
    if myStack == []:
        return True
    return False

def pilha_push(elem):
    myStack.append(elem)
    return

def pilha_pop():
    if pilha_vazia() == True:
        return None
    current = myStack.pop(-1)
    return current

def retList():
    print('My list:', myList)
    # print('My stack:', myStack)
    return myList

myList=[]
myStack=[]
