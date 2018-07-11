## Self Check ##
# To make sure you understand how operators are implemented in Python classes, and how to properly write methods, write some methods to implement *, /, and −. Also implement com- parison operators > and <.


# Base Class
class Fraction:
    # init value
    def __init__(self, top, buttom):
        self.numerator = top
        self.denominator = buttom


    # Convert into string
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    # Override __add__ method
    def __add__(self, other_fraction_value):
        # Common denominator
        new_denominator = self.denominator*other_fraction_value.denominator
        #
        new_numerator = (self.numerator*other_fraction_value.denominator)+(other_fraction_value.numerator*self.denominator)
        common = gcd(new_numerator, new_denominator)
        #最大公約数を得た後、その数で割る。
        return Fraction(new_numerator//common, new_denominator//common)

    # Override __eq__ method
    def __eq__(self, other):
        first_numerator = self.numerator*other.denominator
        second_numerator = other.numerator*self.denominator

        return first_numerator == second_numerator

    # Override __mul__ method
    def __mul__(self, other):
        mul_numerator = self.numerator*other.numerator
        mul_denominator = self.denominator*other.denominator
        greatest_common_denominator = gcd(mul_numerator, mul_denominator)
        return Fraction(mul_numerator//greatest_common_denominator, mul_denominator//greatest_common_denominator)

    # Override __truediv__ method
    def __truediv__(self, other):
        div_numerator = self.numerator*other.denominator
        div_denominator = self.denominator*other.numerator
        greatest_common_denominator = gcd(div_numerator, div_denominator)
        return Fraction(div_numerator/greatest_common_denominator, div_denominator/greatest_common_denominator)

    # Override __sub__ method
    def __sub__(self, other):
        # Common denominator
        new_denominator = self.denominator*other.denominator
        new_numerator = (self.numerator*other.denominator)-(other.numerator*self.denominator)
        common = gcd(new_numerator, new_denominator)
        #最大公約数を得た後、その数で割る。
        return Fraction(new_numerator//common, new_denominator//common)

    # Override __gt__ method
    def __gt__(self, other):
        first_numerator = self.numerator*other.denominator
        second_numerator = other.numerator*self.denominator
        if first_numerator > second_numerator:
            return True
        if first_numerator == second_numerator:
            return False
        if first_numerator < second_numerator:
            return False

# Get the GCD(greatest common dividor) by using Euclid's Algorithm
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n

    return n


# my_f = Fraction(3,5)
# print(my_f)
# print("I ate", my_f, "of the pizza.")
# print(my_f.__str__())
f1 = Fraction(4, 3)
f2 = Fraction(3, 6)
f3 = f1+f2
print(f3)
print(f1==f2)
print(f1*f2)
print(f1/f2)
print(f1-f2)
print(f1>f2)
