## BinaryTree ##
# init argument (root): type str() or int().
# Modules you can access
# print()
# insert_left(new_node_value): type str() or int()
# insert_right(new_node_value): type str() or int()
# get_left_child()
# get_root_value()
# get_right_child()
# set_root_value(new_root_value): type str() or int()

from stack import Stack

class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return str(self.key)

    def __str__(self):
        return str(self.key)

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

        return None

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

        return None

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key

# stk = Stack()
# bt = BinaryTree(1)
# current_tree = bt
# current_tree.insert_left(None)
# current_tree.insert_right(None)
# print("root: ", current_tree.get_root_value())
# print("left: ", current_tree.get_left_child())
# print("right: ", current_tree.get_right_child())
# current_tree.insert_left(2)
# print("root no change: ", current_tree.get_root_value())
# print("left inserted: ", current_tree.get_left_child())
# print("right no change: ", current_tree.get_right_child())
# stk.push(current_tree)
# current_tree = current_tree.get_left_child()
# print("left: ", current_tree.get_left_child()) # None
# print("right: ", current_tree.get_right_child()) # None
# # current_tree.get_left_child().set_root_value(100)
# current_tree.insert_left(3)
#
# current_tree = stk.pop()
#
# print("updated result for left ch root: ", bt.get_left_child().get_root_value())
