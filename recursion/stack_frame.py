import sys
sys.path.insert(0, "./../data_structures/stacks")
from first_stack_practice import Stack


stk = Stack()


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    #
    while n > 0:
        if n > base:
            stk.push(base)
        else:
            # Just push the remainder to the stack.
            stk.push(convert_string[n % base])

        n = n //base

    #
    res = ""
    while not stk.is_empty():
        res = stk

    return res



print(to_str(10, 2))
