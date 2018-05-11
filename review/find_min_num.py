numOfList = [678,834,678,467,834]


# O(n^2) solution
def find_min_one(listOfNums):
    smallest_num = listOfNums[0]
    for i in range(len(listOfNums)):
        for second_num in listOfNums:
            if smallest_num > second_num:
                smallest_num = second_num

    return smallest_num


print(find_min_one(numOfList))



# O(n)

def find_min_two(listOfNums):
    if len(listOfNums) > 2:
        smallest_num = listOfNums[0]
        if listOfNums[0] < listOfNums[1]:
            smallest_num = listOfNums[0]
            listOfNums.pop(1)
            return find_min_two(listOfNums)
        else:
            listOfNums.pop(0)
            return find_min_two(listOfNums)

    else:
        return listOfNums[0]



# print(find_min_two(numOfList))
