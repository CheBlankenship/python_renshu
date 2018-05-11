class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)
        return None

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return [] == self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
