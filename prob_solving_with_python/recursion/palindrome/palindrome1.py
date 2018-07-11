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
    input_str = input_str.replace(" ", "").replace("’", "").replace(",", "").replace(".", "").replace(";", "").upper()
    input_str = list(input_str)
    return checker(input_str)




print(palindrome_checker("Go hang a salami; I’m a lasagna hog."))






#### Authors Example ####

# def helper(s1, s2):
#     if s1 == s2:
#         return True
#     return False
#
# def removeWhite(s):
#     excludes = ("'", ',', ';', '.', ' ')
#     return "".join(ch.upper() for ch in s if ch not in excludes)
#
# def isPal(s):
#     s = removeWhite(s)
#     if len(s) <= 1:
#         return True
#     else:
#         return helper(s[0],s[-1]) and isPal(s[1:-1])
#
#
# print(isPal("reviled did I live, said I, as evil I did deliver"))
#
# print(isPal("Go hang a salami; I'm a lasagna hog."))
# print(isPal("radar"))
# print(isPal(""))
