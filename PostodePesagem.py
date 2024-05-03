n, f, p = map(int, input().split())

posto = []
tempoTotal = 0

posto = input().split()

checagem = f

while len(posto) > 0:

    if checagem == f:
        if int(posto[0]) <= p:
            tempoTotal += 5
            posto.pop(0)
            checagem = 1
        else:
            tempoTotal += 10
            posto.append(int(posto.pop(0)) - 2)
            checagem = 1
    else:
        tempoTotal += 1
        checagem += 1
        posto.pop(0)

print(tempoTotal)
            