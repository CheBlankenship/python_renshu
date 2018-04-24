import time

def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum+1


    end = time.time()
    run_time = end-start
    print(run_time)
    return str(run_time)+"s"


print(sum_of_n(100000))
