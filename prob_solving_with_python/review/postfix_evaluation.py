class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return 0 == len(self.items)


def arithmetic_opration(notation, first_operand, second_operand):

    if notation == "*":
        return first_operand * second_operand

    if notation == "/":
        return first_operand / second_operand

    if notation == "+":
        return first_operand + second_operand

    if notation == "-":
        return first_operand - second_operand



def postfixEvaluation(postfix_expression):

    operand_stack = Stack()
    postfix_expression = list(postfix_expression.replace(" ", ""))

    for token in postfix_expression:

        if token in "0123456789":
            operand_stack.push(int(token))

        if token in "*/+-":
            second_operand = operand_stack.pop()
            first_operand = operand_stack.pop()
            result = arithmetic_opration(token, first_operand, second_operand)
            operand_stack.push(result)

        else:
            return "Maybe there is a alphabet in your postfix expression.."

    return operand_stack.pop()


print(postfixEvaluation("78+32+/"))
