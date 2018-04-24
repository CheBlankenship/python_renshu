import time


# n(n+1)/2
# Example num = 5
# 5(5+1)/2 = 5*6/2 = 15
# 1+2+3+4+5 = 15
# o(1)
def sum_of_n_two(num):
    return num*(num+1)/2


re = sum_of_n_two(50000)
print(re)
