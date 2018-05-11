class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)
        return None

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return [] == self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]




def balanced_parentheses_checker(symbol_str):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_str) and balanced :
        symbol = symbol_str[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index +1


    if balanced and s.is_empty():
        return True
    else:
        return False



def matches(top, symbol):
    open_sym = "({["
    close_sym = "]})"
    return open_sym.index(top) == close_sym.index(symbol)





print(balanced_parentheses_checker('{{([][])}()}'))
print(balanced_parentheses_checker('[{()}]'))
