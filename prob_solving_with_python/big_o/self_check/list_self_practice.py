# Given a list of numbers in random order write a linear time algorithm to find the 𝑘th smallest number in the list. Explain why your algorithm is linear.

import random

# arr = [1, 2, 3]
# arr = list(str(random.randrange(10000)))

def get_smallest_num(arr):
    smallest_num = arr[0]
    for i in range(len(arr)-1):
        if smallest_num > arr[i]:
            smallest_num = arr[i]

    return smallest_num


list_of_num = [random.randrange(10000) for _ in range(10)]
re = get_smallest_num(list_of_num)
print("Result >>> ", re)
