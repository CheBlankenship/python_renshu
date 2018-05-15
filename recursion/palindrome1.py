def checker(input_str):
    matching = True
    if len(input_str) < 2:
        return True
    else:
        while matching:
            if input_str[0] == input_str[-1]:
                input_str = input_str[1:-1]
                return palindrome_checker("".join(input_str))
            else:
                return False



def palindrome_checker(input_str):
    input_str = input_str.replace(" ", "").replace("'", "").replace(",", "").replace(".", "").upper()
    input_str = list(input_str)
    return checker(input_str)




print(palindrome_checker("kAyak"))
