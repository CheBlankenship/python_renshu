

def correct_sentence(text: str) -> str:
    return_text = ""
    modify_text = list(text)
    modify_text[0] = modify_text[0].upper()
    if modify_text[len(modify_text)-1] != ".":
        modify_text.append(".")

    return_text = return_text.join(modify_text) # join the list back to a string
    return return_text



# Another solution example by 3rd party
def correct_sentence_example(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")




string_one = correct_sentence("hello, this is Che Blankenship")
string_two = correct_sentence("hello, this is Che Blankenship using 3rd party solution")
print("Result one >> ", string_one)
print("Result two >> ", string_two)
