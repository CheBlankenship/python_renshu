from tree_node import TreeNode
import operator

class BinarySearchTree:

    def __init__(self, arg):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, current_node.left_child)
        else:
            current_node.left_child = TreeNode(key, val)

        self.size = self.size + 1
