from collections import deque

def bfsMenorCaminho(redeSocial, origem, destino):
    visitados = set()
    fila = deque([(origem, 0)])

    if origem == destino:
        return 0

    while fila:
        atual, distancia = fila.popleft()

        if atual == destino:
            return distancia - 1

        if atual not in visitados:
            visitados.add(atual)
            for contatos in redeSocial.get(atual, []):
                if contatos not in visitados:
                    fila.append((contatos, distancia + 1))
    
    return "Forevis alonis..."

n = int(input())
redeSocial = {}

for i in range(n):
    entrada = [int(x) for x in input().split()]
    id = entrada[0]
    a = entrada[1]
    redeSocial[id] = entrada[2:]

eu, mussum = map(int, input().split())

resultado = bfsMenorCaminho(redeSocial, eu, mussum)
print(resultado)
