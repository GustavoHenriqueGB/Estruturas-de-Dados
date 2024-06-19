def estudaraNoite(n, casosdeTeste):
    resultados = []
    for i in range(n):
        planoEstudos = casosdeTeste[i][0]
        matutino = casosdeTeste[i][1]
        vespertino = casosdeTeste[i][2]
        noturno = casosdeTeste[i][3]

        planoContagem = {}
        for conteudo in planoEstudos:
            if conteudo in planoContagem:
                planoContagem[conteudo] += 1
            else:
                planoContagem[conteudo] = 1

        turnosContagem = {}
        for conteudo in matutino + vespertino + noturno:
            if conteudo in turnosContagem:
                turnosContagem[conteudo] += 1
            else:
                turnosContagem[conteudo] = 1

        for conteudo in turnosContagem:
            if conteudo not in planoContagem:
                resultados.append("You died!")
                break
            elif turnosContagem[conteudo] > planoContagem[conteudo]:
                resultados.append("You died!")
                break
        else:
            conteudosNaoAbordados = []
            for conteudo, quantidade in planoContagem.items():
                if conteudo not in turnosContagem or turnosContagem[conteudo] < quantidade:
                    conteudosNaoAbordados.append(conteudo)

            if not conteudosNaoAbordados:
                resultados.append("It's in the box!")
            else:
                conteudosaEstudar = sorted(conteudosNaoAbordados)
                resultados.append("Bora ralar: " + "".join(conteudosaEstudar))

    return resultados

n = int(input())
casosdeTeste = []

for _ in range(n):
    planoEstudos = input()
    matutino = input()
    vespertino = input()
    noturno = input()
    casosdeTeste.append((planoEstudos, matutino, vespertino, noturno))

resultados = estudaraNoite(n, casosdeTeste)
for resultado in resultados:
    print(resultado)