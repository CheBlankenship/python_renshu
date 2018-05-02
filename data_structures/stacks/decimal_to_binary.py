from first_stack_practice import Stack


def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        print("dec_num >> ", dec_number)
        remain = dec_number % 2
        print("rem >> ", remain)
        rem_stack.push(remain)
        dec_number = dec_number // 2
        print("stack >> ", rem_stack)

    bin_string = ""
    while not rem_stack.is_empty():
        print("bin str >> ", type(str(rem_stack.pop)))
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


print(divide_by_2(43))


# 例１ #
# 43/2=21...1
# 21/2=10...1
# 10/2=5...0
# 5/2 =2...1
# 2/2 =1...0
# 1/2 =0...1
# [1, 1, 0, 1, 0, 1]


# 例２ #
# 22/2=11...0
# 11/2=5...1
# 5/2 =2...1
# 2/2 =1...0
# 1/2 =0...1
# [0, 1, 1, 0, 1]
