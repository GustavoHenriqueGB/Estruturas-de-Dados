class Roupa:

    def __init__(self, tipe, color, time):
        self.tipe = tipe
        self.color = color
        self.time = time

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


roupas = []
n = int(input())
pilha = Stack()

for i in range(n):
    tipo, cor, tempo = input().split()
    pecas = Roupa(tipo, cor, int(tempo))
    roupas.append(pecas.tipe)

print(roupas)
print(pecas)