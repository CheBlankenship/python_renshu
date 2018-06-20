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
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in "+-*/":
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = p_stack.pop()
        elif i not in "()+*-/":
            current_tree.set_root_value(int(i))
            parent = p_stack.pop()
            current_tree = parent
        else:
            raise Exception("ValueError")

    return e_tree

parse_tree = build_pars_tree("((10+5)+(100+50))")

print("root     ", parse_tree.get_root_value())
print("check l  ", parse_tree.get_left_child())
print("check l l", parse_tree.get_left_child().get_left_child())
print("check l r", parse_tree.get_left_child().get_right_child())
print("check r  ", parse_tree.get_right_child())
print("check r l", parse_tree.get_right_child().get_left_child())
print("check r r", parse_tree.get_right_child().get_right_child())
# print("check ", parse_tree)
# print("check ", parse_tree)

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



def inorder(tree):
    t_str = ""
    if tree:
        t_str = "(" + inorder(tree.get_left_child())
        t_str = t_str + str(tree.get_root_value())
        t_str = inorder(tree.get_right_child()) + ")"

    return t_str


# print("Result >>", inorder(parse_tree))


def preorder(tree):
    if tree:
        print("Root >> ", tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


# print("Result >> ", preorder(parse_tree))



def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print("Root >> ", tree.get_root_value())

# print("Result >> ", postorder(parse_tree))
