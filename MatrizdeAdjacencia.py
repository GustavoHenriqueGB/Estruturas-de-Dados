v, e, c = input().split()
v = int(v)
e = int(e)

matriz = [[0 for _ in range(v)] for _ in range(v)]

if c == 'N':
    for i in range(e):
        x, y, z = map(int, input().split())
        matriz[x - 1][y - 1] = z
        matriz[y - 1][x - 1] = z
else:
    for i in range(e):
        x, y, z = map(int, input().split())
        matriz[x - 1][y - 1] = z

for i in range(v):
    for j in range(v):
        print(f"{matriz[i][j]:4d}", end='')
    print()