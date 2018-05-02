# Basic stack class

class Stack():
    # init
    def __init__(self):
        self.items = []
    #
    def __str__(self):
        # return "%s" % self.items
        return str(self.items)

    # Check if items is empty if its empty it'll return True, else False.
    def is_empty(self):
        return self.items == []
    # Add item to items
    def push(self, item):
        self.items.append(item)
    #
    def pop(self):
        return self.items.pop()
    #
    def peek(self):
        return self.items[len(self.items)-1]
    #
    def size(self):
        return len(self.items)


# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s)

# s.push('x')
# s.push('y')
# s.pop()
# s.push('z')
# print(s.peek())

# an error will occur
# m = Stack()
# m.push('x')
# m.push('y')
# m.push('z')
# print(m)
# while not m.is_empty():
#     m.pop()
#     m.pop()
#
# print(m)
