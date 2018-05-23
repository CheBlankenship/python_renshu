# Time complexity : O(n^2)

def selection_sort(num_list):
    for fill_slot in range(len(num_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            print("pos >> ", pos_of_max, " loc >> ", location)
            if num_list[location] > num_list[pos_of_max]:
                pos_of_max = location

        temp = num_list[fill_slot]
        num_list[fill_slot] = num_list[pos_of_max]
        num_list[pos_of_max] = temp
        print("Replaced >> ",num_list[fill_slot],  " : ", num_list[pos_of_max])

    return num_list

num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# fill_slot = 8
# [(54), (26), 93, 17, 77, 31, 44, 55, 20] , ps = 0, lo = 1, F
# [(54), 26, (93), 17, 77, 31, 44, 55, 20] , ps = 0, lo = 2, T
# [54, 26, (93), (17), 77, 31, 44, 55, 20] , ps = 2, lo = 3, F
# [54, 26, (93), 17, (77), 31, 44, 55, 20] , ps = 2, lo = 4, F
# .........
# .........
# [54, 26, (93), 17, (77), 31, 44, 55, 20] , ps = 2, lo = 8, F
# After the second for loop #
# Replace list[ps]...93 and list[fill_slot(last index of the array)]...20


print(selection_sort(num_list))
