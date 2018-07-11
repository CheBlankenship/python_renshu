from first_stack_practice import Stack


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = Stack()

    while dec_number > 0:
        rem_number = dec_number % base
        rem_stack.push(rem_number)
        dec_number = dec_number // base

    new_str = ""
    while not rem_stack.is_empty():
        new_str = new_str + digits[rem_stack.pop()]


    return new_str


print(base_converter(567, 16))
