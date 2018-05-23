def quick_sort(num_list):
    re = quick_sort_helper(num_list, 0, len(num_list) - 1)
    return re

def quick_sort_helper(num_list, first, last):
    if first < last:
        split_point = partition(num_list, first, last)
        quick_sort_helper(num_list, first, split_point - 1)
        quick_sort_helper(num_list, split_point + 1, last)

    return num_list


def partition(num_list, first, last):
    pivot_value = num_list[first]

    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while (left_mark <= right_mark) and (num_list[left_mark] <= pivot_value):
            left_mark = left_mark + 1

        while (num_list[right_mark] >= pivot_value) and (right_mark >= left_mark):
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temporary = num_list[left_mark]
            num_list[left_mark] = num_list[right_mark]
            num_list[right_mark] = temporary

    temporary = num_list[first]
    num_list[first] = num_list[right_mark]
    num_list[right_mark] = temporary


    return right_mark



num_list = [5,16,20,3,8,12,9,17,20,7]
print(quick_sort(num_list))
