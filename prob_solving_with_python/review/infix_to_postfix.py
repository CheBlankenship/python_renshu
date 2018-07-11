# Basic Instruction for converting infix to postfix expression #
# 1. Create an empty stack called op_stack for keeping operators. Create an empty list for output.
# 2. Convert the input infix string to a list by using the string method split.
# 3. Scan the token list from left to right.
# • If the token is an operand, append it to the end of the output list.
# • If the token is a left parenthesis, push it on the op_stack.
# • If the token is a right parenthesis, pop the op_stack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
# • If the token is an operator, *, /, +, or −, push it on the op_stack. However, first remove any operators already on the op_stack that have higher or equal precedence and append them to the output list.


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

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return int(len(self.items))


# s = Stack()
# s.push("a")
# s.push("b")
# print(s.peek())



def infix_to_postfix(infix_expression):
    op_stack = Stack()
    output = []
    infix_expression = list(infix_expression.replace(" ", ""))
    precedences = {}
    precedences["*"] = 3
    precedences["/"] = 3
    precedences["+"] = 2
    precedences["-"] = 2
    precedences["("] = 1

    operand = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for token in infix_expression:
        print("output >> ", output)
        if token in operand:
            output.append(token)

        if token == "(":
            op_stack.push(token)

        if token == ")":
            while op_stack.pop() != "(":
                output.append(op_stack.pop())

        if token in "*/+-":
            # print("target >> ", op_stack.peek())
            while not op_stack.is_empty() and (precedences[op_stack.peek()]) >= (precedences[str(token)]):
                print("HIT", precedences[op_stack.peek()])
                output.append(op_stack.pop())

            op_stack.push(token)



    while not op_stack.is_empty():
        output.append(op_stack.pop())


    return "".join(output)



print(infix_to_postfix("A * B + C * D"))



















#
