class Fila:

    def __init__(self):
        self.queue = []

    def is_Empty(self):
        return len(self.queue) == 0

    def chegada(self, nome):
        self.queue.append(nome)

    def saida(self):
        if not self.is_Empty():
             return self.queue.pop()
         
    def movimento(self, movimentos):
        for i in range(movimentos):
            if not self.is_Empty():
              self.queue.append(self.queue.pop(0))

    def primeiro(self):
        if not self.is_Empty():
            return self.queue[0]
    
    def ultimo(self):
        if not self.is_Empty():
            return self.queue[len(self.queue) - 1]

    
lista = input().split()
fila = Fila()
numero = int(input())

for i in lista:
    fila.chegada(i)

fila.movimento(numero)

print(f"Pessoa da frente: {fila.primeiro()}")
print(f"Pessoa do fim: {fila.ultimo()}")