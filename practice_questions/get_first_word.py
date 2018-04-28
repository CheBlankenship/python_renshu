# return the first word in a given text.

# My solution
def first_word(text: str) -> str:
    result = ""
    text_in_list = text.replace(",", " ").replace(".", " ").split(" ")[0]
    print("arr >> ", text_in_list)
    still_ok = True
    index_num = 0
    while range(len(text_in_list)) and still_ok:
        if len(text_in_list[index_num]) > 0 and still_ok:
            still_ok = False
            result = text_in_list[index_num]
        else:
            print("check word >> ", text_in_list[index_num])
            still_ok = True
            index_num = index_num + 1


    return result

print(first_word("and so on"))


# 3rd party solution
import re
def first_word(text: str) -> str:
    words = re.split(r"[,. ]", text)
    words = [word for word in words if len(word) > 0]
    return words[0]
