import random

class PrintQueue:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)
        return None

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return [] == self.items

    def size(self):
        return len(self.items)
