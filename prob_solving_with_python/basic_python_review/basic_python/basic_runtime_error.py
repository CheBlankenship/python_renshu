import math

input_num = input("Enter number >> ")

if float(input_num) > 0:
    print(math.sqrt(float(input_num)))
else:
    raise RuntimeError("You can't use a negative number!")
