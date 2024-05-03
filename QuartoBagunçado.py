class Roupa:

    def __init__(self, tipe, color, time):
        self.tipe = tipe
        self.color = color 
        self.time = time
        

class Stack:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


roupas = []
tempoTotal = 0
n = int(input())
pilha = Stack()

for i in range(n):
    tipo, cor, tempo = input().split()
    pilha.push(Roupa(tipo, cor, int(tempo)))


while not pilha.isEmpty():
    roupa = pilha.pop()
    print(f"Tipo: {roupa.tipe}, Cor: {roupa.color}")
    tempoTotal += roupa.time

print(f"Total de roupas: {n}")
print(f"Total de tempo: {tempoTotal}")