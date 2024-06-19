def inverterLista(L):
    previous = None
    current = L.head
    while current is not None:
        next_node = current.getNext()
        current.setNext(previous)
        previous = current
        current = next_node
    L.head = previous
    return L 