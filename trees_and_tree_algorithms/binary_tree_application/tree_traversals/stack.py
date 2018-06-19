class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.insert(0, item)
        return None

    def pop(self, pos=0):
        if pos != 0 and int(pos) == int:
            self.items.pop(pos)
        else:
            self.items.pop(0)

    def peek(self):
        if (not self.is_empty()):
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return [] == self.items

#
