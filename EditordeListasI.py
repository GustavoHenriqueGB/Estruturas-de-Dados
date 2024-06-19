ans = []

while True:

    n = input()
    lista = n.split()
    
    if lista[0] == "I":
        ans.insert(0, int(lista[1]))
        
    elif lista[0] == "F":
        ans.append(int(lista[1]))
        
    elif lista[0] == "P":
        if ans:
            print(ans.pop())
            
    elif lista[0] == "D":
        if ans:
            print(ans.pop(0))
            
    elif lista[0] == "X":
        for i in range(len(ans)):
            print(ans[i])
        break

