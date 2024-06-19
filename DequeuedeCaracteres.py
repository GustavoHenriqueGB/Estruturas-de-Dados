class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
entrada = input()
fila = Queue()

for i in entrada: 

    if i == "*":
        print(fila.dequeue(), end="")

    else:
         fila.enqueue(i)