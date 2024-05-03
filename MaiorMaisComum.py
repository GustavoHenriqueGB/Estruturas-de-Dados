def substrings(palavra):
    lista = []

    for i in range(len(palavra)):
        substring = ''

        for j in range(len(palavra) - i):
            substring += palavra[i+j]
            lista.append(substring)
          
    return lista

maiorTamanho = count = 0
existentes = []

sarscov1 = input()
influenza = input()

subSas1 = substrings(sarscov1)
subSas2 = substrings(influenza)

for sub in subSas2:
    if sub in subSas1:
       existentes.append(sub)
       
       if len(sub) > maiorTamanho:
           maiorTamanho = len(sub)

for sub in existentes:
    if len(sub) == maiorTamanho:
        count += 1

print(len(sarscov1))
print(len(influenza))
print(maiorTamanho)