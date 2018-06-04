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

def hanoi_count(number_of_plates):
    # 2 ^ n - 1
    return ((2 ** number_of_plates) - 1)



print(hanoi_count(5))
