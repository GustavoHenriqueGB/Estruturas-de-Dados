from math import ceil
x = int(input())

print(f"Transmitindo {x} bytes...")

n = count = count1 = 0
taxa = []

while n != x:
    n += int(input())
    count += 1
   
    taxa.append(n)
    if len(taxa) > 5:
        taxa.pop(0)
    
    if x - n == 0:
        pass
    else:
        
        if count - count1 >= 5:
            count1 = count

            if len(taxa) == 5:
                media = (n - taxa[0])/5
                if media > 0:
                    br = x - n
                    tr = ceil(br/ media)
                    print(f"Tempo restante: {tr} segundos.")
                else:
                    print("Tempo restante: pendente...")

            else:
                print("Tempo restante: pendente...")


print(f"Tempo total: {count} segundos.")