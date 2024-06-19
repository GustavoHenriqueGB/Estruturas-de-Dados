t, n = map(int, input().split())
lista =[]
tabela = {i: [] for i in range(t)}

if n !=0:
    for i in input().split():
        lista.append(int(i))

for chave in lista:
    indice = chave % t
    tabela[indice].append(chave)

for chave in tabela.keys():
    valores = tabela[chave]
    
    if len(valores)< 1:
        print(f"{chave} - [x]")
        
    else:
        print(f"{chave} -", end=" ")
        
        if len(valores) > 1:
            for i in range(len(valores)):
                if i != (len(valores) - 1):
                    print(f"{valores[i]} -> ", end="")
                    
                else:
                    print(f"{valores[i]}")
                
        elif len(valores) == 1:
            print(f"{valores[0]}")