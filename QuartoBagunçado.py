class Roupa:

    def __init__(self, tipo, cor, tempo_dobrar):
        self.tipo = tipo
        self.cor = cor
        self.tempo_dobrar = tempo_dobrar

class PilhaDeRoupas:
    def __init__(self):
        self.roupas = []
        self.total_roupas = 0
        self.tempo_total = 0

    def adicionar_roupa(self, roupa):
        self.roupas.append(roupa)
        self.total_roupas += 1
        self.tempo_total += roupa.tempo_dobrar

    def organizar(self):
        gaveta = []
        for roupa in self.roupas:
            gaveta.append((roupa.tipo, roupa.cor))
        return gaveta, self.total_roupas, self.tempo_total


n = int(input())

for i in range(n - 1):
    pilha = PilhaDeRoupas()
    entrada = input().split()

    tipo, cor, tempo_dobrar = input().split()
    roupa = Roupa(tipo, cor, int(tempo_dobrar))
    pilha.adicionar_roupa(roupa)
    
gaveta, total_roupas, tempo_total = pilha.organizar()
    
print("Roupas na gaveta:")
for roupa in gaveta:
    print(f"{roupa[0]} {roupa[1]}")
print(f"Total de roupas: {total_roupas}")
print(f"Tempo total: {tempo_total} minutos\n")

