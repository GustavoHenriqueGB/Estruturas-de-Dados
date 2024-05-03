class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
entrada = input()
pilha = Stack()

for i in entrada:

    if i == "*":
        print(pilha.pop(), end="")

    else:
        pilha.push(i)