def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[int(n)]
    else:
        return to_str(int(n) / base, base) + convert_string[int(n) % base]


print(to_str(16, 2))
