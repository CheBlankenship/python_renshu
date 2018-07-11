import math

a_num = input("Enter number >> ")

try:
    print(math.sqrt(float(a_num)))
except Exception as e:
    print("Bad value for square root.")
    print("Using absolute value instead.")
    print(math.sqrt(abs(int(a_num))))
