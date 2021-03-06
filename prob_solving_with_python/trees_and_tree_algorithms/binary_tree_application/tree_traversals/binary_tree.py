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



class BinaryTree:

    def __init__(self, root):
        self.root       = root
        self.left_child = None
        self.right_child= None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, new_node_value):
        if self.get_left_child() == None:
            self.left_child = BinaryTree(new_node_value)
        else:
            t = BinaryTree(new_node_value)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node_value):
        if self.right_child == None:
            self.right_child = new_node_value
        else:
            t = BinaryTree(new_node_value)
            t.right_child = self.right_child
            self.right_child = t

    def get_root_value(self):
        return self.root

    def set_root_value(self, obj):
        self.root = obj
        return None
