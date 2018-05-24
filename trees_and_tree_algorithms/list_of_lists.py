def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    print("check >> ", t)
    if len(t) > 1:
        root.insert(1, [new_branch, t, [] ])
    else:
        root.insert(1, [new_branch, [], [] ])

    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root



def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val
    return None

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


# lOl = binary_tree(1)
# lOl2 = binary_tree(2)
rot = []
print(insert_left([1, [], []], 1))
# print(lOl)
