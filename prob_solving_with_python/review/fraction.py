class Fraction():

    # Init values
    def __init__(self, num, den):
        self.num = num
        self.den = den
        greatest_common_denominator = gcd(self.num, self.den)
        self.numerator = num//greatest_common_denominator
        self.denominator = den//greatest_common_denominator



    def get_num(self):
        return self.numerator

    def get_den(self):
        return self.denominator

    ## Override the built-in arithmetic operators
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, other):
        denominator_add = self.denominator*other.denominator
        numerator_add = (self.numerator*other.denominator)+(other.numerator*self.denominator)
        return Fraction(numerator_add, denominator_add)

    def __sub__(self, other):
        denominator_sub = self.denominator*other.denominator
        numerator_sub = (self.numerator*other.denominator)-(other.numerator*self.denominator)
        greatest_common_denominator = gcd(self.num, self.den)
        return Fraction(numerator_sub//greatest_common_denominator, denominator_sub//greatest_common_denominator)

    def __mul__(self, other):
        denominator_mul = self.denominator*other.denominator
        numerator_mul = self.numerator*other.numerator
        greatest_common_denominator = gcd(self.num, self.den)
        return Fraction(numerator_mul//greatest_common_denominator, denominator_mul//greatest_common_denominator)



def gcd(num, den):
    while den % num != 0:
        numerator = num
        denominator = den
        num = denominator % numerator
        den = numerator

    return num


f1 = Fraction(8,9)
f2 = Fraction(5,7)
# print(f.get_num())
# print(f.get_den())
print("result >> ", f1+f2)
print("result >> ", f1-f2)
print("result >> ", f1*f2)
