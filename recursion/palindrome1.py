def string_converter(input_str):
    matching = True
    input_str = input_str.replace(" ", "").replace("'", "").replace(",", "").replace(".", "")
    input_str = list(input_str)
    if len(input_str) < 2:
        return True
    else:
        while matching:
            if input_str[0] == input_str[-1]:
                input_str = input_str[1:-1]
                return palindrome_checker("".join(input_str))
            else:
                return False




print(palindrome_checker("kayak"))
