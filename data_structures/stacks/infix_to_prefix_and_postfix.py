# from first_stack_practice import Stack


# Instruction #
# 1. Create an empty stack called op_stack for keeping operators. Create an empty list for output.
# 2. Convert the input infix string to a list by using the string method split.
# 3. Scan the token list from left to right.
#   • If the token is an operand, append it to the end of the output list.
#   • If the token is a left parenthesis, push it on the op_stack.
#   • If the token is a right parenthesis, pop the op_stack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
#   • If the token is an operator, *, /, +, or −, push it on the op_stack.
#     However, first remove any operators already on the op_stack that have higher or equal precedence and append them to the output list.
# When the input expression has been completely processed, check the op_stack.
# Any operators still on the stack can be removed and appended to the end of the output list.


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)




# s = Stack()
# s.push("ew")
# s.push("ww")
# print(s.size())





def infix_to_postfix(infix_str):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = list(infix_str.replace(" ", ""))

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())

            op_stack.push(token)


    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
        return "".join(postfix_list)



print(infix_to_postfix("( A + B ) * ( C + D )"))
