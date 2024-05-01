n = int(input())

for i in range(n):
    frase = input()

    for i in len(frase):
        if ord(frase[i]) == 40 or ord (frase[i])== 91 or ord(frase[i]) == 123: 
            if frase[i + 1] == 40 or frase[i + 1] == 91 or frase[i + 1] == 123: