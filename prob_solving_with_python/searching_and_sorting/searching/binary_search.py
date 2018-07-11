# O(logn)
def binary_search(num_list, num):
    first = 0
    last = len(num_list) - 1
    found = False

    while first <= last and not found:
        mid_position = (first + last) // 2
        if num_list[mid_position] == num:
            found = True
        else:
            if num < num_list[mid_position]:
                last = mid_position - 1
            else:
                first = mid_position + 1

    return found


num_list = [0,1,2,3,4,5,6,6,7,8,9]
print(binary_search(num_list, 100))
# print(binary_search(test_list, 13))
