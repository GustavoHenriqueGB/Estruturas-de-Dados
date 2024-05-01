class Posto:
    
    def __init__(self):
        self.fila = []

    def __init__(self):
        self.fator = 1

    def __init__(self):
        self.maxpeso = 0

    def fatoramostragem(self, numero):
        self.fator = numero

    def pesomax(self, numero):
        self.maxpeso = numero

    def chegada(self, carro):
        self.fila.append(carro)

    def isEmpty(self):
        return len(self.fila) == 0

    def checagem(self, maxpeso, fator):
        count = 1
        if not self.isEmpty():
            for i in range(0, len(self.fila), fator):
                if self.fila[i] <= maxpeso:
















n , f , p = int(input().split())
veiculos = input().split()