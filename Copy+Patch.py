x = int(input())

print(f"Transmitindo {x} bytes...")

taxaBy = n = count = count1 = 0

while n < x:
    y = int(input())
    taxaBy += y
    n += y
    restante = x - n
    
    count += 1
    count1 += 1

    if count1 == 5:
        taxa_atual = taxaBy/count1
        if taxa_atual != 0:
            if restante != 0:
                print(f"Tempo restante: {round((restante)/taxa_atual + 0.499)} segundos.")
        
        else:
            print("Tempo restante: pendente...")
        taxaBy = count1 = 0
    
       
print(f"Tempo total: {count} segundos.")
