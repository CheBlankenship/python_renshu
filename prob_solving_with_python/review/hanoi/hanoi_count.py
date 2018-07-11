import sys
# import os
sys.path.insert(0, "./../../data_structures/stacks")
from first_stack_practice import Stack




# Count how many times you need to move to get the goal.

# Hanoi Tower approach #
# Examples #
# N(1) = 1 time
# N(2) = 3 times
# N(3) = 7 times
# N(4) = 15 times
# N(5) = 31 times
# Process #
# Move 2(n-1)+ 1
# Move + 1
# Move 2(n-1) + 1
# Therefore :  A(n) = (2 * A(n-1))+ 1 == 2 ^ n - 1

def hanoi_count(num):
    # 2 ^ n - 1
    return ((2 ** num) - 1)

print(hanoi_count(30))



def hanoi_simulation(number_of_plates):
    stk_one = Stack()
    stk_two = Stack()
    stk_three = Stack()
    number_of_moves = hanoi_count(number_of_plates)
    # print("Count >> ", number_of_moves)
    # stk_one.push("1")
    # stk_two.push("2")
    # stk_three.push("3")


    return str(stk_one) + "\n" + str(stk_two) + "\n" + str(stk_three)


print(hanoi_simulation(1))
