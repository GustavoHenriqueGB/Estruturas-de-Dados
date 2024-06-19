m, n = map(int, input().split())

lista = [int (x) for x in input().split()]
ans = []

for i in range(m - n + 1):
    media = sum(lista[i:i + n]) / n
    
    print(int(round(media - 0.4999)))
