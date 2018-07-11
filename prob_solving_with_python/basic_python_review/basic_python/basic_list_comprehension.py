# Example one
square_list_one = []

for item in range(1, 11):
    square_list_one.append(item*item)

print(square_list_one)


# Example two(list comprehension)
square_list_two = [item*item for item in range(1, 11)]
print(square_list_two)


# Example three(only even number)
square_list_three = [item*item for item in range(1, 11) if item*item %2==0]
print(square_list_three)


# Example four(only "aeiou")
aeiou_list = [item for item in "comprehension" if item in "aeiou"]
print(aeiou_list)
