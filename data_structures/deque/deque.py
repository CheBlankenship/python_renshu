class Dequeue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def add_rear(self, item):
        self.items.insert(0, item)
        return None

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return [] == self.items

    def size(self):
        return len(self.items)


d = Dequeue()
d.add_rear("a")
d.add_rear("b")
d.add_rear("c")
d.add_rear("d")
d.remove_rear()
d.remove_front()
print(d.is_empty())
print(d.size())
print("Result >> ", d)
