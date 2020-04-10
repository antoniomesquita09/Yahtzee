__all__=['exibe', 'lst_vazia', 'lst_insIni', 'lst_insFin', 'lst_retIni', 'lst_retFin']

def lst_vazia():
    if myList==[]:
        return True
    return False

def lst_insIni(elem):
    myList.insert(-1, elem)

def lst_insFin(elem):
    myList.append(elem)

def lst_retIni():
    myList.pop(0)

def lst_retFin():
    myList.pop(-1)

def exibe():
    if lst_vazia() == True:
        print('lista vazia true')
        return
    print('lista vazia false:', myList)

myList=[0]
