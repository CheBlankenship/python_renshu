# Example one
def sum_of_n(n):
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum+1

    return the_sum


# Example two : bad example
def foo(tom):
    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred = fred + barney

    return fred


## What to compare ##
# One way is to consider the amount of space or memory an algorithm requires to solve the problem.
# As an alternative to space requirements, we can analyze and compare algorithms based on the amount of time they require to execute.


# Better solution
# 階乗を用いた方法
def efficient_sum_of_n(n):
    return (n*(n+1))/2
