def shell_sort(num_list):
    sublist_count = len(num_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(num_list, start_position, sublist_count)
            # print("After increments of size", sublist_count, "The list is", num_list)
        sublist_count = sublist_count // 2

    return num_list


def gap_insertion_sort(num_list, start, gap):
    # print("num_list >> ", num_list, " start >> ", start, " gap >> ", gap)
    for i in range(start + gap, len(num_list), gap):
        current_value = num_list[i]
        position = i
        while (position >= gap) and (num_list[position - gap] > current_value):
            num_list[position] = num_list[position - gap]
            position = position - gap

        num_list[position] = current_value




num_list = [4, 53, 65, 77, 87, 88, 90, 7686]
print(shell_sort(num_list))
