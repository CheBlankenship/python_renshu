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
plot_list_one = []

t1 = Timer("find_min_one([1])", "from __main__ import find_min_one")
plot_list_one.append(t1.timeit(number=1000))
t2 = Timer("find_min_one([1,2])", "from __main__ import find_min_one")
plot_list_one.append(t2.timeit(number=1000))
t3 = Timer("find_min_one([1,2,3])", "from __main__ import find_min_one")
plot_list_one.append(t3.timeit(number=1000))
t4 = Timer("find_min_one([4,5,6,7])", "from __main__ import find_min_one")
plot_list_one.append(t4.timeit(number=1000))
t5 = Timer("find_min_one([4,5,6,7,34])", "from __main__ import find_min_one")
plot_list_one.append(t5.timeit(number=1000))
t6 = Timer("find_min_one([4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t6.timeit(number=1000))
t7 = Timer("find_min_one([3,81,44,52,452,1,99])", "from __main__ import find_min_one")
plot_list_one.append(t7.timeit(number=1000))
t8 = Timer("find_min_one([1,2,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t8.timeit(number=1000))
t9 = Timer("find_min_one([1,2,3,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t9.timeit(number=1000))
t10 = Timer("find_min_one([4,5,6,7,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t10.timeit(number=1000))
t11 = Timer("find_min_one([4,5,6,7,34,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t11.timeit(number=1000))
t12 = Timer("find_min_one([4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t12.timeit(number=1000))
t13 = Timer("find_min_one([1,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t13.timeit(number=1000))
t14 = Timer("find_min_one([1,2,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t14.timeit(number=1000))
t15 = Timer("find_min_one([1,2,3,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t15.timeit(number=1000))
t16 = Timer("find_min_one([4,5,6,7,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t16.timeit(number=1000))
t17 = Timer("find_min_one([4,5,6,7,34,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t17.timeit(number=1000))
t18 = Timer("find_min_one([4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t18.timeit(number=1000))
t19 = Timer("find_min_one([1,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t19.timeit(number=1000))
t20 = Timer("find_min_one([1,2,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t20.timeit(number=1000))
t21 = Timer("find_min_one([1,2,3,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t21.timeit(number=1000))
t22 = Timer("find_min_one([4,5,6,7,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t22.timeit(number=1000))
t23 = Timer("find_min_one([4,5,6,7,34,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t23.timeit(number=1000))
t24 = Timer("find_min_one([4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_one")
plot_list_one.append(t24.timeit(number=1000))




plot_list_two = []
t1 = Timer("find_min_two([1])", "from __main__ import find_min_two")
plot_list_two.append(t1.timeit(number=1000))
t2 = Timer("find_min_two([1,2])", "from __main__ import find_min_two")
plot_list_two.append(t2.timeit(number=1000))
t3 = Timer("find_min_two([1,2,3])", "from __main__ import find_min_two")
plot_list_two.append(t3.timeit(number=1000))
t4 = Timer("find_min_two([4,5,6,7])", "from __main__ import find_min_two")
plot_list_two.append(t4.timeit(number=1000))
t5 = Timer("find_min_two([4,5,6,7,34])", "from __main__ import find_min_two")
plot_list_two.append(t5.timeit(number=1000))
t6 = Timer("find_min_two([4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t6.timeit(number=1000))
t7 = Timer("find_min_two([1,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t7.timeit(number=1000))
t8 = Timer("find_min_two([1,2,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t8.timeit(number=1000))
t9 = Timer("find_min_two([1,2,3,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t9.timeit(number=1000))
t10 = Timer("find_min_two([4,5,6,7,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t10.timeit(number=1000))
t11 = Timer("find_min_two([4,5,6,7,34,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t11.timeit(number=1000))
t12 = Timer("find_min_two([4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t12.timeit(number=1000))
t13 = Timer("find_min_two([1,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t13.timeit(number=1000))
t14 = Timer("find_min_two([1,2,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t14.timeit(number=1000))
t15 = Timer("find_min_two([1,2,3,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t15.timeit(number=1000))
t16 = Timer("find_min_two([4,5,6,7,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t16.timeit(number=1000))
t17 = Timer("find_min_two([4,5,6,7,34,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t17.timeit(number=1000))
t18 = Timer("find_min_two([4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t18.timeit(number=1000))
t19 = Timer("find_min_two([1,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t19.timeit(number=1000))
t20 = Timer("find_min_two([1,2,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t20.timeit(number=1000))
t21 = Timer("find_min_two([1,2,3,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t21.timeit(number=1000))
t22 = Timer("find_min_two([4,5,6,7,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t22.timeit(number=1000))
t23 = Timer("find_min_two([4,5,6,7,34,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t23.timeit(number=1000))
t24 = Timer("find_min_two([4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81,4,5,6,7,3,81])", "from __main__ import find_min_two")
plot_list_two.append(t24.timeit(number=1000))



plt.title("Algoritm Time Complexity")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.plot(plot_list_one, 'r--', label = 'O(n^2)')
plt.plot(plot_list_two, 'g^', label = 'O(n)')
plt.legend()
plt.show()
