# Best case : O(1 - n/2)
# Avg case  : O(n/2 - n)
# Worst case: O(n)

def seq_search(item_list, search_v):
    pos = 0
    found = False
    while (pos < len(item_list)) and (not found):
        if search_v == item_list[pos]:
            found = True
        else:
            pos = pos + 1
    return found



item_list = [6, 3, 9, 10, 6]


print(seq_search(item_list, 0))
