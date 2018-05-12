class Deque:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    def add_front(self, item):
        self.items.append(item)
        return None

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




# d = Deque()
# print(d.is_empty())
# print(d.size())

def palindrome_checker(input_str):
    d = Deque()
    matching = True
    for char in input_str:
        d.add_rear(char)

    while matching and d.size() > 1:
        front = d.remove_front()
        rear = d.remove_rear()
        if front != rear:
            matching = False

    return matching

input_str = "ccvd"
print(palindrome_checker(input_str))
