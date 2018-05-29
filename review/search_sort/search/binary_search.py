# If the item list is in order use binary searchself.
# Best case :
# Avg case  :
# Worst case:

def binary_search(item_list, search_v):
    start = 0
    last = len(item_list) - 1
    found = False

    while (start <= last) and (not found):
        mid = int((start + last) // 2)
        if search_v == item_list[mid]:
            found = True
        else:
            if item_list[mid] < search_v:
                start = start + 1
            else:
                last = last - 1

    return found



# item_list = [2, 4, 6, 7, 9, 10, 11, 23, 45]
# print("result >> ", binary_search(item_list, 6))



# Use recursive
def b_search(item_list, search_v):
    if len(item_list) == 0:
        return False
    else:
        mid = len(item_list) // 2
        if search_v == item_list[mid]:
            return True
        else:
            if search_v > item_list[mid]:
                return b_search(item_list[mid + 1: ], search_v)
            else:
                return b_search(item_list[ : mid], search_v)



# item_list = [2, 4, 6, 7, 9, 10, 11, 23, 45]
# print("result >> ", b_search(item_list, 4))
