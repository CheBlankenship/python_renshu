def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[int(n)]
    else:
        # Return the next converting number and the remainder.
        return to_str(int(n) / base, base) + str(convert_string[int(n) % base])


print(to_str(16, 2))
