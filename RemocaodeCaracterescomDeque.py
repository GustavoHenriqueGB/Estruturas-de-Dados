from collections import deque

entrada = input()
lista = deque([])

for i in range(len(entrada)):
    if entrada[i].isnumeric():
        lista.append(entrada[i])
        
    elif entrada[i] == '*':
        print(lista.popleft(), end= "")
    elif entrada[i] == '+':
        print(lista.pop(), end= "")
    else:
        lista.appendleft(entrada[i])
    
