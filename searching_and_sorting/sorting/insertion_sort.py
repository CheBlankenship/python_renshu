def insertion_sort(num_list):

    for index in range(1, len(num_list)):
        current_value = num_list[index]
        position = index

        while (position > 0) and (num_list[position - 1] > current_value):
            num_list[position] = num_list[position - 1]
            position = position - 1

        num_list[position] = current_value

    return num_list



num_list = [4,87,90,77,65,53,7686,4,88]
print(insertion_sort(num_list))

# Step By Step #
# [4, 87, 90, 90, 65, 53, 7686, 4, 88], current_value = 77
