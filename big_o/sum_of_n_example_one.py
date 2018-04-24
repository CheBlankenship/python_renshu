import time

# O(n)
def sum_of_n_one(num):
    result = 0
    for i in range(num+1):
        print(i)
        result = result + i

    return result

re = sum_of_n_one(50000)
print(re)
