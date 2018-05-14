# Process of converting infix into prefix expression #
# 1, Reverse infix expression
# 2, convert it into postfix expression
# 3, Reverse it to prefix expression


# First In Last Out
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




def infix_to_prefix(infix_expression):
    operators = {}
    operators["*"] = 3
    operators["/"] = 3
    operators["+"] = 2
    operators["-"] = 2
    operators["("] = 1
    stack_for_operands = Stack()
    output_list = []

    infix_li = list(infix_expression.replace(" ", ""))
    # Reverse infix expression
    reverse_infix = []
    for i in range(len(infix_li)-1, -1, -1):
        # print(infix_li[i])
        if infix_li[i] == "(":
            infix_li[i] = ")"
            reverse_infix.append(infix_li[i])
        elif infix_li[i] == ")":
            infix_li[i] = "("
            reverse_infix.append(infix_li[i])
        else:
            reverse_infix.append(infix_li[i])


    print(reverse_infix)

    still_convert = True
    for token in reverse_infix:
        # If the token is an operand, append it to the end of the output list.
        if token in "ABCDEFGHIJKLMNOPQRSTUXYZ0123456789":
            output_list.append(token)

        # If the token is a left parenthesis, push it on the op_stack.
        elif token == "(":
            stack_for_operands.push(token)

        elif token == ")":
            pop_from_stack = stack_for_operands.pop()
            while pop_from_stack != "(":
                output_list.append(pop_from_stack)
                pop_from_stack = stack_for_operands.pop()


        elif token in "*/+-":
            while (not stack_for_operands.is_empty()) and (not operators[token] <= operators[stack_for_operands.peek()]):
                    output_list.append(stack_for_operands.pop())
            stack_for_operands.push(token)


    print("Left >> ", stack_for_operands)
    while not stack_for_operands.is_empty():
        output_list.append(stack_for_operands.pop())


    print("out ", output_list)
    result = "".join(output_list)
    return result



print(infix_to_prefix("( A + B ) * ( C + D )"))





# [C, B, A]
# ("+", "(", "*", ")")
