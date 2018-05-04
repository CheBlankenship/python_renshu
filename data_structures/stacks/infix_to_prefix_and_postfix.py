from first_stack_practice import Stack


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


# input  -> string(infix format)
# output -> string(prefix and postfix format)

def convert_infix_to_prefix_and_postfix(input_str):
    op_stack = Stack()
    input_list = list(input_str)
    return input_list



print(convert_infix_to_prefix_and_postfix("gofd"))
