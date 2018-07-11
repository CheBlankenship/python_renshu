import timeit
from timeit import Timer

# Compare the time complexity between dictionary and list
l = list(range(100000))
d = {j: j for j in range(100000)}

print(d[2])


def pop_list():
    l.pop(5)

def pop_dict():
    d.pop(5)


list_time = Timer("pop_list", "from __main__ import pop_list")
dict_time = Timer("pop_dict", "from __main__ import pop_dict")

print("List >> ", list_time.timeit(number=100000))
print("Dict >> ", dict_time.timeit(number=100000))
