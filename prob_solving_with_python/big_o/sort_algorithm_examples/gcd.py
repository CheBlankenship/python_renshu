# GCD(Greatest Common Divisor) function

def gcd(num1, num2):
    set_n1 = num1
    set_n2 = num2

    while set_n1 % set_n2 != 0:
        n2 = set_n1 - (set_n1 // set_n2 * set_n2)
        n1 = set_n2
        set_n1 = n1
        set_n2 = n2

    return set_n2


print(gcd(32, 20))
