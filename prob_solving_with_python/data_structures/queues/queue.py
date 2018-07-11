class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return [] == len(items)

    # Set the rear as index 0
    def enqueue(self, item):
        self.items.insert(0, item)

    # Set the front as index len(self.items)-1
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.enqueue('hello'))
print(q.enqueue('dog'))
print(q.enqueue(3))
print(q.dequeue())
print(q)
