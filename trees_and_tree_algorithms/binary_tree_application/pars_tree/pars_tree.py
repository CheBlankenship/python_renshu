# 1. Create an empty tree.
# 2. Read ( as the first token.
# By rule 1, create a new node as the left child of the root. Make the current node this new child.
# 3. Read 3 as the next token.
# By rule 3, set the root value of the current node to 3 and go back up the tree to the parent.
# 4. Read + as the next token.
# By rule 2, set the root value of the current node to + and add a new node as the right child. The new right child becomes the current node.
# 5. Read a ( as the next token.
# By rule 1, create a new node as the left child of the current node. The new left child becomes the current node.
# 6. Read a 4 as the next token.
# By rule 3, set the value of the current node to 4. Make the parent of 4 the current node.
# 7. Read * as the next token.
# By rule 2, set the root value of the current node to * and create a new right child. The new right child becomes the current node.
# 8. Read 5 as the next token.
# By rule 3, set the root value of the current node to 5. Make the parent of 5 the current node.
# 9. Read ) as the next token.
# By rule 4 we make the parent of * the current node.
# 10. Read ) as the next token.
# By rule 4 we make the parent of + the current node. At this
point there is no parent for + so we are done.

class ClassName(object):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
