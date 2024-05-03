class Fifo:

    def __init__(self):
        self.fila = []

    def chegou(self, valor):
        self.fila.append(valor)

    def isEmpty(self):
        return len(self.fila) == 0

    def saiu(self):
        if not self.isEmpty():
            return self.fila.pop(0)
    
class Aipo:

    def __init__(self):
        self.prioridade = []

    def chegou(self, valor):
        self.prioridade.append(valor)
        self.prioridade.sort()

    def isEmpty(self):
        return len(self.prioridade) == 0

    def saiu(self):
        if not self.isEmpty():
            return self.prioridade.pop()
    
class Lifo:

    def __init__(self):
        self.pilha = []

    def chegou(self, valor):
        self.pilha.append(valor)

    def isEmpty(self):
        return len(self.pilha) == 0

    def saiu(self):
        if not self.isEmpty():
            return self.pilha.pop()
    
for i in range(5):
    x = int(input())
    fbool = abool = lbool = 0

    fifo = Fifo()
    aipo = Aipo()
    lifo = Lifo()

    for j in range(x):
        
        check, num = input().split()
        num = int(num)
        if check == "in":
            fifo.chegou(num)
            aipo.chegou(num)
            lifo.chegou(num)

        elif check == "out":
            if fifo.saiu() == num:
                fbool += 1
            if lifo.saiu() == num:
                lbool += 1
            if aipo.saiu() == num:
                abool += 1
        
    if fbool > lbool and fbool > abool:
        print("FIFO")
    elif abool > lbool and abool > fbool:
        print("AIPO")
    elif lbool > fbool and lbool > abool:
        print("LIFO")
    elif fbool == abool or lbool == abool:
        print("uai?")
    else:
        print("no hay!")