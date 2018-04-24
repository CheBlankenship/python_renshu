# Write two Python functions to find the minimum number in a list.


arr = [5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,5,6,8,99,1]

# The first function should compare each number to every other number on the list. 𝑂(𝑛^2).
# ###
# The second function should be linear 𝑂(𝑛).
def find_min_num_two(arr):
    min_number = arr[0]
    for i in range(len(arr)):
        if min_number > arr[i]:
            min_number = arr[i]

    return min_number

re1 = find_min_num_two(arr)
# print(re1)
