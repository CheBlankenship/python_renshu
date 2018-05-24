# List of lists
list_tree = [1, \
    [2, \
        [4, \
            [8], [11]\
        ],\
        [5, \
            [9], [12]\
        ]\
    ], \
    [3, \
        [6, \
            [10], [13] \
        ], \
        [7]\
    ]\
]

print("Tree >> ", list_tree)
print("Root >> ", list_tree[0])
print("Sub tree 1 >> ", list_tree[1])
print("Sub tree 2 >> ", list_tree[2])
