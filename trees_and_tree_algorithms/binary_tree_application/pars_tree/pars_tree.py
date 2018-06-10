## Pars Tree ##


from stack import Stack
from binary_tree import BinaryTree
import operator

def conv_list(input):
    li = []
    concat_num = ""
    for item in input:
        if item in "()+*-/":
            if len(concat_num) > 0 :
                li.append(concat_num)
                concat_num = ""

            li.append(item)
        else:
            concat_num = concat_num + item

    return li




def build_pars_tree(fp_exp):
    fp_list = conv_list(fp_exp)
    p_stack = Stack()
    e_tree  = BinaryTree("")
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        # print("i >> ", i)
        if i == "(":
            # print("HIT 1")
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in "+-*/":
            # print("HIT 2")
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            # print("HIT 3")
            current_tree = p_stack.pop()
        elif i not in "()+*-/":
            # print("HIT 4")
            current_tree.set_root_value(int(i))
            parent = p_stack.pop()
            current_tree = parent
        else:
            # print("HIT 5")
            raise Exception("ValueError")

    return e_tree

print("return ", build_pars_tree("((10+5)*3)"))


def evaluate(parse_tree):
    opers = {}
    opers["+"] = operator.add
    opers["-"] = operator.sub
    opers["*"] = operator.mul
    opers["/"] = operator.truediv

    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_value()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_value()
