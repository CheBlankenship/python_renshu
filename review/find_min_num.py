import matplotlib.pyplot as plt
import timeit
import random
from timeit import Timer


numOfList = [678,834,678,467,834]


# O(n^2) solution
def find_min_one(listOfNums):
    smallest_num = listOfNums[0]
    for i in range(len(listOfNums)):
        for second_num in listOfNums:
            if smallest_num > second_num:
                smallest_num = second_num

    return smallest_num


# print(find_min_one(numOfList))



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

# Visualize the time complexity #
plot_list = []

t1 = Timer("find_min_one([1,2,3])", "from __main__ import find_min_one")
plot_list.append(t1.timeit(number=1000))
t2 = Timer("find_min_one([1,2,3,4,5,6,7])", "from __main__ import find_min_one")
plot_list.append(t2.timeit(number=1000))
t3 = Timer("find_min_one([1,2,3,4,5,6,7,8,9,0,1,32,4,4])", "from __main__ import find_min_one")
plot_list.append(t3.timeit(number=1000))
t4 = Timer("find_min_one([4,5,6,7,3,7,8,1,5,6,8,5,1,2,3,4,5,6,7,8,9,0,1,32,4,4])", "from __main__ import find_min_one")
plot_list.append(t4.timeit(number=1000))
t5 = Timer("find_min_one([4,5,6,7,3,7,8,1,5,6,8,5,1,2,3,4,5,6,7,8,9,0,1,32,4,4,1,2,3,4,5,6,7,8,9,0,1,32,4,4])", "from __main__ import find_min_one")
plot_list.append(t5.timeit(number=1000))
t6 = Timer("find_min_one([4,5,6,7,3,7,8,1,5,6,8,5,1,2,3,4,5,6,7,8,9,0,1,32,4,4,1,2,3,4,5,6,7,8,9,0,1,32,4,4,6,7,3,7,8,1,5,6,8,5,1,2,3,4,5,6,7,8,9,0,1,32,4,4,1])", "from __main__ import find_min_one")
plot_list.append(t6.timeit(number=1000))



plt.plot(plot_list, 'ro')
plt.ylabel('Time complexity')
plt.show()
