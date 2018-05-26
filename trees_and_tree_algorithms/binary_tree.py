class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_ch = None
        self.right_ch = None

    def __repr__(self):
        return str(self.key)

    def __str__(self):
        return str(self.key)


    def insert_left(self, new_node):
        if self.left_ch == None:
            self.left_ch = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_ch = self.left_ch
            self.left_ch = t
        return None

    def insert_right(self, new_node):
        if self.right_ch == None:
            self.right_ch = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_ch = self.right_ch
            self.right_ch = t
        return None

    def get_right_child(self):
        return self.right_ch

    def get_left_child(self):
        return self.left_ch

    def set_root_val(self, obj):
        self.key = obj
        return None

    def get_root_val(self):
        return self.key


# bt = BinaryTree(1)
# bt.insert_left(2)
# bt.insert_right(3)
# bt.set_root_val()
# print("root > " ,bt)
# print("left > " ,bt.left_ch)
# print("right > " ,bt.right_ch)

# insert into pre-exist node
# bt.insert_left(4)
# print("root > " ,bt)
# print("left1 > " ,bt.left_ch)
# print("right1 > " ,bt.right_ch)
# print("left2 > " ,bt.left_ch.left_ch)
# print("right2 > " ,bt.right_ch.right_ch)
# print(bt.get_root_val())
# print(bt.get_right_child())
# print(bt.get_left_child())
# print(bt.set_root_val("hola"))
#
# print(bt.get_root_val())


def build_tree():
    bt = BinaryTree("a")
    bt.insert_right("c")
    bt.insert_left("b")
    bt.left_ch.insert_right("d")
    # bt.left_ch.insert_left()
    bt.right_ch.insert_right("f")
    bt.right_ch.insert_left("e")

    print("Root >> ", bt)
    print("Left  1 >> ", bt.get_left_child())
    print("Right 1 >> ", bt.get_right_child())
    print("Right 1 Left  2 >>", bt.get_right_child().left_ch)
    print("Right 1 Right 2 >>", bt.get_right_child().right_ch)
    print("Left  1 Left  2 >> ", bt.get_left_child().left_ch)
    print("Left  1 Right 2 >> ", bt.get_left_child().right_ch)


    #

build_tree()


# Result #
# $ python3 binary_tree.py
# Root >>  a
# Left  1 >>  b
# Right 1 >>  c
# Right 1 Left  2 >> e
# Right 1 Right 2 >> f
# Left  1 Left  2 >>  None
# Left  1 Right 2 >>  d
