def exibe_candidatos(deque, pos, ordem):
    tamanhoFinal = deque.size() - pos

    if tamanhoFinal > deque.size() or deque.is_empty() or pos < 0 or pos > deque.size():
        return
    
    if ordem == "direta":
        while deque.size() > tamanhoFinal:
            deque.remove_front()
        
    elif ordem == "inversa":
        while deque.size() > pos + 1:
            deque.remove_rear()

    while not deque.is_empty():
        if ordem == "direta":
            print(deque.remove_front())
        
        elif ordem == "inversa":
            print(deque.remove_rear())
