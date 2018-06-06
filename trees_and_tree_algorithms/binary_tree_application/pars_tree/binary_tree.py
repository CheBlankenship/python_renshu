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

    def insert_right(self, new_node):
        pass
