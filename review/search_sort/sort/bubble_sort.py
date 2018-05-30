def basic_sort(item_list):
    pos = 0
    while pos < len(item_list):
        for i in range(len(item_list) - 1):
            if item_list[i] > item_list[i + 1]:
                temp = item_list[i]
                item_list[i] = item_list[i + 1]
                item_list[i + 1] = temp

        pos = pos + 1

    return item_list






# item_list = [5,6,1, 8,8,999,34,24,56,77,0]
# print(basic_sort(item_list))




def bubble_sort(item_list):
    pass
