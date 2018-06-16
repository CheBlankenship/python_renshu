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
    step = 0
    for i in fp_list:
        step = step + 1
        print("{step ", step, "}", i)
        if i == "(":
            current_tree.insert_left("")
            print("current_tree : ", current_tree.get_root_value(), current_tree.get_left_child(), current_tree.get_right_child())
            p_stack.push(current_tree)
            print("stack :", p_stack)
            current_tree = current_tree.get_left_child()
        elif i in "+-*/":
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            print("current_tree ; ", current_tree.get_root_value(), current_tree.get_left_child(), current_tree.get_right_child())
            p_stack.push(current_tree)
            print("stack :", p_stack)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = p_stack.pop()
            print("stack :", p_stack)
        elif i not in "()+*-/":
            current_tree.set_root_value(int(i))
            print("stackk :", p_stack.size())
            parent = p_stack.pop()
            print("stack :", p_stack)
            print("Current tree >> ", "[", current_tree.get_root_value() ,current_tree.get_left_child(), current_tree.get_right_child(), "]")
            print("parent       >> ", "[", parent.get_root_value() ,parent.get_left_child(), parent.get_right_child(), "]")
            current_tree = parent
            print("current      >>> ", "[", current_tree.get_root_value() ,current_tree.get_left_child(), current_tree.get_right_child(), "]")
            print("Previouse >> ", parent.get_left_child())
        else:
            raise Exception("ValueError")

    print("Tree >> ", e_tree.get_root_value(), e_tree.get_left_child(), e_tree.get_right_child(), e_tree.get_left_child().get_left_child(), e_tree.get_left_child().get_right_child())
    return e_tree

parse_tree = build_pars_tree("(10+5)")


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
        # fn = add(left, right) || sub(left, right) || mul(left, right) || truediv(left, right)
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_value()


print(evaluate(parse_tree))
#
