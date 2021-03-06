# Time Complexity #
# Best  : O(n^2)
# Avg   : O(n^2)
# Worst : O(n^2)
def bubble_sort(num_list):
    for num in range(len(num_list)-1, 0, -1):
        for li_index in range(num):
            if num_list[li_index] > num_list[li_index + 1]:
                # Swap : a, b = b, a
                temporary_def = num_list[li_index]
                num_list[li_index] = num_list[li_index + 1]
                num_list[li_index + 1] = temporary_def

    return num_list

num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# num = 8, li_index = 0 ~ 8
# [54, 26, 93, 17, 77, 31, 44, 55, 20]
# [26, 54, 93, 17, 77, 31, 44, 55, 20]
# [26, 54, 17, 93, 77, 31, 44, 55, 20]
# [26, 54, 17, 77, 93, 31, 44, 55, 20]
# [26, 54, 17, 77, 31, 93, 44, 55, 20]
# [26, 54, 17, 77, 31, 44, 93, 55, 20]
# [26, 54, 17, 77, 31, 44, 55, 93, 20]
# [26, 54, 17, 77, 31, 44, 55, 20, 93]

# num = 7, li_index = 0 ~ 7
# :
# num = 6, li_index = 0 ~ 6
# :
# :
# :
# num = 0, li_index = 0

print("Result 1 >> ", bubble_sort(num_list))


# Author's Example

def sort_bubble_sort(num_list):
    exchanges = True
    pass_num = len(num_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if num_list[i] > num_list[i + 1]:
                exchanges = True
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]

    return num_list



print("Result 2 >> ", sort_bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
