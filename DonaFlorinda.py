def chaveOrdenacao(pretendente):
    nome, sobrenome, altura, massa = pretendente
    distanciaAltura = abs(180 - altura)
    distanciaMassa = 0 if massa == 75 else 1
    if massa < 75:
        return (distanciaAltura, distanciaMassa, 0, abs(massa - 75), sobrenome.lower(), nome.lower())
    else:
        return (distanciaAltura, distanciaMassa, 1, abs(massa - 75), sobrenome.lower(), nome.lower())

n = int(input())
pretendentes = []

for _ in range(n):
    entrada = input().split()
    nome = entrada[0]
    sobrenome = entrada[1]
    altura = int(entrada[2])
    massa = int(entrada[3])
    pretendentes.append((nome, sobrenome, altura, massa))

pretendentesOrdenados = sorted(pretendentes, key=chaveOrdenacao)

for pretendente in pretendentesOrdenados:
    nome, sobrenome, _, _ = pretendente
    print(f"{sobrenome}, {nome}")