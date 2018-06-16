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

    def pop(self, position=0):
        if position != 0:
            return self.items.pop(position)
        else:
            return self.items.pop(0)

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
# s = Stack()
# s.push("")
# s.push(None)
# s.push(3)
# s.push(4)
# print(s)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# print(s)
# print(s.peek())
# print(s.size())
# print(s.is_empty())
