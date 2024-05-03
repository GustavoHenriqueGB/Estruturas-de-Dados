class Pesos:

    def __init__(self):
        self.stack =[]

    def push(self, peso):
        self.stack.append(peso)

    def pop(self):
        return self.stack.pop()


    def is_Empty(self):
        return self.stack == []
    
    def peek(self):
        if not self.is_Empty():
            return self.stack[-1]
    
    def search(self, anilha):
        retiradas = []
        while (not self.is_Empty()) and anilha != self.peek():
            retiradas.append(self.pop())
        if not self.is_Empty():
            retiradas.append(self.pop())
        return retiradas
        
pilha = Pesos()
tiradas = []
pesoTotal = 0

while True:
    x = int(input())
    if x == 0:
        break
    else:
        pilha.push(x)

if not pilha.is_Empty(): 
    peso = int(input())
    tiradas = pilha.search(peso)

    if tiradas:  
        for i in tiradas:
            print(f"Peso retirado: {i}")

        print(f"Anilhas retiradas: {len(tiradas)}")
        print(f"Peso total movimentado: {sum(tiradas)}")
