
def hash(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum = sum + ord(a_string[pos])

    return sum % table_size


h = hash("My name is ... ", 5)
print("result >> ", h)


# Process #

# Example : hash("cat", table_size)
# ord(c) -> 99
# ord(a) -> 97
# ord(t) -> 116
# return ((99+97+116) % table_size)
