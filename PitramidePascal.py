def triangulo(n):
    piramide = []

    for i in range(n):
        linha = [1] * (i+1)
        if i >= 1:
            for j in range(1, i):
                linha[j] = piramide[i - 1][j - 1] + piramide[i - 1][j]
        piramide.append(linha)

    return piramide


