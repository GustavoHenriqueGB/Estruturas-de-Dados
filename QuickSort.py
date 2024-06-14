def quickSort(alist):
    if len(alist) <=1:
        return alist
    esquerda, pivo, direita = reordena(alist)
    esquerda = quickSort(esquerda)
    direita = quickSort(direita)
    esquerda.append(pivo)
    esquerda.extend(direita)
    return esquerda

def reordena(alist):
    pivo = alist[0]

    esquerda = []
    direita = []

    for n in range(1, len(alist)):
        aux = alist[n]
        if aux <= pivo:
            esquerda.append(aux)
        else:
            direita.append(aux)

    return esquerda, pivo, direita




print(quickSort([3,4,6,1,2,5]))