# Stack class


class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return 0 == len(self.items)

    # return last item in the list
    def peek(self):
        return self.items[len(self.items)-1]


# 1. Create an empty stack called operand_stack.
# 2. Convert the string to a list by using the string method split. 3. Scan the token list from left to right.
# • If the token is an operand, convert it from a string to an integer and push the value onto the operand_stack.
# • If the token is an operator, *, /, +, or −, it will need two operands. Pop the operand_stack twice.
#   The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation.
#   Push the result back on the operand_stack.
# 4. When the input expression has been completely processed, the result is on the stack. Pop the operand_stack and return the value.


def postfix_evaluation(postfix_expression):
    operand_stack = Stack()
    token_list = list(postfix_expression.replace(" ", ""))

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            second_operand = operand_stack.pop()
            first_operand = operand_stack.pop()
            result = do_math(token, first_operand, second_operand)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(operator, operand_one, operand_two):
    if operator == "*":
        return operand_one * operand_two

    if operator == "/":
        return operand_one / operand_two

    if operator == "+":
        return operand_one + operand_two

    if operator == "-":
        return operand_one - operand_two



print(postfix_evaluation("7 8 + 3 2 + /"))
