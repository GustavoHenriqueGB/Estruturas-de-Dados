def altura(arvore):
    if not arvore:
        return 0
    
    altura_esquerda = altura(arvore[1])
    altura_direita = altura(arvore[2])
    
    return 1 + max(altura_esquerda, altura_direita)