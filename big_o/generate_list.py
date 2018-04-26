import timeit
from timeit import Timer

# Check which is the fastest way to generate a list

# 1 - Use a for loop and concatinate(list + list).
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

    return l

# print(test1())

# 2 - Use a for loop and append the integer to the list.
def test2():
    l = []
    for i in range(1000):
        l.append(i)

    return l

# print(test2())

# Use list comprehension.
def test3():
    l = [int for int in range(1000)]
    return l

# print(test3())

# Use list() method.
def test4():
    l = list(range(1000))
    return l


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
