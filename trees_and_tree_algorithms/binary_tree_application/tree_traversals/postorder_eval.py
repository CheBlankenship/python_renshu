# Evaluate the tree using postorder approach.
from stack import Stack
from binary_tree import BinaryTree
import operator

def post_eval(tree):
    opers = {}
    opers["+"] = operator.add
    opers["-"] = operator.sub
    opers["*"] = operator.mul
    opers["/"] = operator.truediv

    if tree:
        post_eval()
