import sys
sys.path.insert(0, "./../data_structures/stacks")
from first_stack_practice import Stack


stk = Stack()


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    #
    while n > 0:
        if n < base:
            stk.push(n)
        else:
            # Just push the remainder to the stack.
            stk.push(convert_string[n % base])

        n = n //base

    #
    res = ""
    while not stk.is_empty():
        res = res + str(stk.pop())

    return res



#print(to_str(10000, 16))




def n_to_str(num, base):
    numstr = "0123456789ABCDEF"
    # When the num comes smaller than the base converter number, just return the num.
    if num < base:
        return numstr[num]
    # Continue making the number smaller.
    else:
        return n_to_str(num//base, base) + str(numstr[num % base])


# print(n_to_str(100, 16))

def test():
    again = 'y'
    while again == 'y':
        try:
            number = int(input('Number to be converted: '))
            base = int(input('Base to be used: '))
        except:
            print("Invalid input. Try again.")
            continue
        
        print('Using nonrecursion')
        print(to_str(number, base))
        print('Using recursion')
        print(n_to_str(number, base))
        again = input('Do you want to  continue with another conversion? y or n: ')


test()
