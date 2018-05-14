# First In Last Out
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

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return [] == self.items
