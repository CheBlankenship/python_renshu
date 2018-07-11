def merge_sort(num_list):

    if len(num_list) > 1:
        mid = len(num_list) // 2
        left_half = num_list[:mid]
        right_half = num_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while (i < len(left_half)) and (j < len(right_half)):
            if left_half[i] < right_half[j]:
                num_list[k] = left_half[i]
                i = i + 1
            else:
                num_list[k] = right_half[j]
                j = j + 1

            k = k + 1


        while i < len(left_half):
            num_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            num_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merge >> ", num_list)

    return num_list



num_list = [5,3,8,7,16,19,9,17,20,12]
print(merge_sort(num_list))
