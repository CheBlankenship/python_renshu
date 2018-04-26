import timeit
from timeit import Timer

# Compare the time complexity between dictionary and list

def generate_l():
    # Generate list
    l = list(range(10000))
    return l


def generate_d():
    # Generate dictionary
    d = {j: None for j in range(10000)}
    return d


list_time = Timer("generate_l", "from __main__ import generate_l")
dict_time = Timer("generate_d", "from __main__ import generate_d")

print(list_time.timeit(number=10000))
print(dict_time.timeit(number=10000))
