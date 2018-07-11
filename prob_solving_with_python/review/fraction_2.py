
class Fraction:

    def __init__(self, numerator, denominator):
        try:
            if type(numerator) is int and type(denominator) is int:
                common = gcd(numerator, denominator)
                self.numerator = numerator // common
                self.denominator = denominator // common
        except TypeError as err:
            print("TypeError >> ", err)


    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __repr__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, other_fraction):
        add_numerator = (self.numerator * other_fraction.denominator) + (other_fraction.numerator * self.denominator)
        add_denominator = self.denominator * other_fraction.denominator
        return Fraction(add_numerator, add_denominator)

    def __radd__(self,other_fraction):
        return __add__(other_fraction)

    def __iadd__(self,other_fraction):
        return __add__(other_fraction)

    def __eq__(self, other_fraction):
        numerator_one = self.numerator*other_fraction.denominator
        numerator_two = other_fraction.numerator*self.numerator
        return numerator_one == numerator_two

    def __sub__(self, other_fraction):
        sub_numerator = (self.numerator * other_fraction.denominator) - (other_fraction.numerator * self.denominator)
        sub_denominator = self.denominator * other_fraction.denominator
        return Fraction(sub_numerator, sub_denominator)

    def __mul__(self, other_fraction):
        mul_numerator = self.numerator * other_fraction.numerator
        mul_denominator = self.denominator * other_fraction.denominator
        return Fraction(mul_numerator, mul_denominator)

    def __truediv__(self, other_fraction):
        div_numerator = self.numerator * other_fraction.denominator
        div_denominator = self.denominator * other_fraction.numerator
        return Fraction(div_numerator, div_denominator)

    def __gt__(self, other_fraction):
        numerator_one = self.numerator*other_fraction.denominator
        numerator_two = other_fraction.numerator*self.numerator
        return numerator_one > numerator_two

    def __ge__(self, other_fraction):
        numerator_one = self.numerator*other_fraction.denominator
        numerator_two = other_fraction.numerator*self.numerator
        return numerator_one >= numerator_two

    def __lt__(self, other_fraction):
        numerator_one = self.numerator*other_fraction.denominator
        numerator_two = other_fraction.numerator*self.numerator
        return numerator_one < numerator_two

    def __le__(self, other_fraction):
        numerator_one = self.numerator*other_fraction.denominator
        numerator_two = other_fraction.numerator*self.numerator
        return numerator_one <= numerator_two

    def __ne__(self, other_fraction):
        numerator_one = self.numerator*other_fraction.denominator
        numerator_two = other_fraction.numerator*self.numerator
        return numerator_one != numerator_two



# Greate Common Divisor
def gcd(numerator, denominator):
    old_numer = numerator
    old_denom = denominator

    while numerator % denominator != 0:
        denominator = old_numer % old_denom
        numerator = old_denom
        old_numer = numerator
        old_denom = denominator

    return old_denom





f =Fraction(-2,4)

print(Fraction(1, -3) + 1/2)
