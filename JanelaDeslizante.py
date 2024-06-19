from collections import deque

n = int(input())

ans = []
lista = []

lista = [int(x) for x in input().split()]

k = int(input())

for i in range(n - k + 1):
    janela = []
    for j in range(k):
        janela.append(lista[i + j])
    ans.append(max(janela))

for i in range(len(ans)):
    print(ans[i], end="  ")
print()