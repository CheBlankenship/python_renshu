class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_ch = None
        self.right_ch = None

    def __repr__(self):
        return str(self.key)

    def __str__(self):
        return str(self.key)

    def get_left_child(self):
        return self.left_ch

    def get_right_child(self):
        return self.right_ch

    def set_root_val(self, val):
        return root.insert(1, [val, [], []])

    def get_root_val(self):
        return self.key
