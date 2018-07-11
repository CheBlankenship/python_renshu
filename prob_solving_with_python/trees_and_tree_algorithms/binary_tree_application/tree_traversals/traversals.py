# Tree Traversals with preorder approach.
# Use recursive call and go though the tree.

from stack import Stack
from binary_tree import BinaryTree
import operator


bt = BinaryTree("")


# Visit root node and recursivly do a preorder on left child and right child.
def preorder(tree):
    if tree:
        print("Root >> ", tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())



# Recursivly do a inorder on left -> node and right.
def inorder(tree):
    t_str = ""
    if tree:
        t_str = "(" + inorder(tree.get_left_child())
        t_str = t_str + str(tree.get_root_val())
        t_str = inorder(tree.get_right_child()) + ")"

    return t_str



# Recursivly do a postorder on left -> right and root.
def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print("Root >> ", tree.get_root_val())
