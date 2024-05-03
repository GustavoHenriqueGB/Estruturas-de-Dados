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
        if self.isEmpty():
            self.fila.append(valor)
        else:
            for i in range(len(self.prioridade) - 1):
                if valor > self.prioridade[i]:
                    self.prioridade.insert(i, valor)

    def isEmpty(self):
        return len(self.fila) == 0

    def saiu(self):
        if not self.isEmpty():
            return self.fila.pop(0)
    
class Lifo:

    def __init__(self):
        self.pilha = []

    def chegou(self, valor):
        self.fila.append(valor)

    def isEmpty(self):
        return len(self.fila) == 0

    def saiu(self):
        if not self.isEmpty():
            return self.fila.pop()
    
