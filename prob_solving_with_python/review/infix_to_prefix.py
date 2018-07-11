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
        return self.items.pop()

    def is_empty(self):
        return [] == self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]




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


    tokenList = reverse_infix
    postfixList = []

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            stack_for_operands.push(token)
        elif token == ')':
            topToken = stack_for_operands.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = stack_for_operands.pop()
        else:
            while (not stack_for_operands.is_empty()) and (operators[stack_for_operands.peek()] >= operators[token]):
                postfixList.append(stack_for_operands.pop())
            stack_for_operands.push(token)

    while not stack_for_operands.is_empty():
        postfixList.append(stack_for_operands.pop())
    return " ".join(postfixList)

    # for token in reverse_infix:
    #     # If the token is an operand, append it to the end of the output list.
    #     if token in "ABCDEFGHIJKLMNOPQRSTUXYZ" or token in "0123456789":
    #         output_list.append(token)
    #
    #     # If the token is a left parenthesis, push it on the op_stack.
    #     elif token == '(':
    #         stack_for_operands.push(token)
    #
    #     elif token == ')':
    #         top_token = stack_for_operands.pop()
    #         while top_token != '(':
    #             output_list.append(top_token)
    #             top_token = stack_for_operands.pop()
    #
    #
    #     else:
    #         while (not stack_for_operands.is_empty()) and (not operators[token] <= operators[stack_for_operands.peek()]):
    #                 output_list.append(stack_for_operands.pop())
    #         stack_for_operands.push(token)
    #
    #
    # print("Left >> ", stack_for_operands)
    # while not stack_for_operands.is_empty():
    #     output_list.append(stack_for_operands.pop())
    #
    #
    # print("out ", output_list)
    # result = "".join(output_list)
    # return result



print(infix_to_prefix("(A*B)+C"))





# [C, B, A]
# ["+", "(", "*", ")"]


#
