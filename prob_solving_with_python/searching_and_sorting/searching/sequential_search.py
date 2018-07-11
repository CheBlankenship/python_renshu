# Best Case   : O(1)
# AVG Case    : O(n/2)
# Worst Case  : O(n)
def sequential_search(item_list, item):
    position = 0
    found = False

    while position < len(item_list) and not found:
        if item_list[position] == item:
            found = True
        else:
            position = position + 1

    return found




arr = [1,2,3,4,5,6,7,88]
print(sequential_search(arr, 10))
