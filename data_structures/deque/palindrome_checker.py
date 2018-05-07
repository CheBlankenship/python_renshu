# Set up a Deque
class Deque:

    def __init__(self):
        self.items = []

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



def palindrome_checker(input_str):
    char_dequeue = Deque()

    for char in input_str:
        char_dequeue.add_rear(char)

    still_eql = True

    while char_dequeue.size() > 1:
        head = char_dequeue.remove_front()
        last = char_dequeue.remove_rear()
        if head != last:
            still_eql = False

    return still_eql


print(palindrome_checker("holalaoh"))
