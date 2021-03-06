class Stack:

    def __init__(self):
        self.items = []

    def __repl__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    # First In Last Out
    def pop(self):
        return self.items.pop(0)

    def push(self, item):
        self.items.insert(0, item)
        return None

    def is_empty(self):
        return [] == self.items

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)




def dec_converter(input_num, converter):
    s = Stack()
    nums = "0123456789ABCDEF"
    still_convert = True

    while still_convert:
        if input_num // converter != 0:
            s.push(str(nums.index(str(input_num % converter))))
            input_num = input_num // converter
        else:
            s.push(str(input_num % converter))
            still_convert = False

    result = ""
    while s.size() > 0:
        result = result+s.pop()

    return result

# 1. What is the value of 25 expressed as an octal number(8)?
print(dec_converter(21, 8))
# 2. What is the value of 256 expressed as a hexidecimal number(16)?
print(dec_converter(21, 16))
