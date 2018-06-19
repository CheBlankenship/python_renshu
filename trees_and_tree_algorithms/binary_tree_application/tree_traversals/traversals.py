# Tree Traversals with preorder approach.
# Use recursive call and go though the tree.
def preorder(tree):
    if tree:
        print("Root >> ", tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
