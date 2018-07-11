# Given code
word_list = ['cat','dog','rabbit']
letter_list = []

# Q1: Modify the given code so that the final list only contains a single copy of each letter.
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:
            letter_list.append(a_letter)

# print(letter_list)


# Q2: Redo the given code using list comprehensions. For an extra challenge, see if you can figure out how to remove the duplicates.
# Be aware of list comprehension side effects.
first_list = [a_letter for a_word in word_list for a_letter in a_word]
second_list = []
[second_list.append(item) for item in first_list if item not in second_list]
print(second_list)
