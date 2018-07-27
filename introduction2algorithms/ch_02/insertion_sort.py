


def insertion_sort(arr):
    # Start out from second index.
    for index in range(1, len(arr)):
        # Set current_value(key) and position.
        current_value = arr[index]
        position = index

        while (position > 0) and (current_value < arr[position - 1]):
            arr[position] = arr[position - 1] # Overwrite the item in index-1.
            position = position - 1 # decrease the loop.

        arr[position] = current_value # Insert the key value at the end.

    return arr

a = [5,8,2]
print(insertion_sort(a))


# - 1 -
# 8
# position = 1
# 8 < 5 = false
# position = 1 (stay 1)
# arr[1] = 8


# - 2 -
# current_value = 2
# position = 2
# arr[2] = arr[1] = 8
# [5, 8, 8]
# 1) position = 1
# 2 < arr[position - 1(0)] = 5
# arr[1] = 5
# [5, 5, 8]
# position = 0
# Exit while loop
# arr[position(0)] = current_value = 2
