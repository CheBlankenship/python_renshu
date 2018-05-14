# First In Last Out
class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.insert(0, item)
        return None

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return [] == self.items



def infix_reverser(infix_expression):
    output_str = ""
    infix_expression_list = list(infix_expression.replace(" ", ""))
    for tkn in range(len(infix_expression_list)-1, -1, -1):
        if infix_expression_list[tkn] == "(":
            infix_expression_list[tkn] = ")"
            output_str = output_str+infix_expression_list[tkn]
        elif infix_expression_list[tkn] == ")":
            infix_expression_list[tkn] = "("
            output_str = output_str+infix_expression_list[tkn]
        else:
            output_str = output_str+infix_expression_list[tkn]

    return prefix_converter(output_str)



# Converter
def prefix_converter(infix_str):
    op_stack = Stack() # Used for keeping operators.
    output = []
    infix_str = list(infix_str.replace(" ", ""))
    print("hey ", infix_str)
    opr = {}
    opr["*"] = 3
    opr["/"] = 3
    opr["+"] = 2
    opr["-"] = 2
    opr["("] = 1

    for token in infix_str:
        if token in "ABCDEFGHIJKLMNOPQRSTUXYZ" or token in "0123456789":
            output.append(token)

        if token == "(":
            op_stack.push(token)

        if token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                print("TOP_TOKEN >> ", top_token)
                output.append(top_token)
                top_token = op_stack.pop()
                print("NEXT >> ", top_token)

            # op_stack.push(token)


        if token in "*/+-":
            print("status >> ", op_stack)
            while (not op_stack.is_empty()) and (opr[op_stack.peek()] >= opr[token]):
                output.append(op_stack.pop())

            op_stack.push(token)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    output = output[::-1]

    return "output >> ", "".join(output)




# print(prefix_converter("C+(A*B)"))
print(infix_reverser("C+(A*B)"))
