# Question 1
# The way we will simulate this is to write a function
# The sentence we’ll shoot for is: “me thinks it is like a weasel”
import random
import time

# 1, that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space.
def attempt(str_len):
    # 26 letters in the alphabet plus the space.
    alphabet = "abcdefghijklmnopqrstuvxyz "
    # print(len(alphabet))
    # Empty str value for storing letters.
    value = ""
    # Loop though 27 times to generate a str that is 27 chars long.
    for letter in range(str_len):
        # Append the value into var value
        # Get a character randomly from str alphabet including space.
        value = value + alphabet[random.randrange(26)]

    return value


# 2, We will write another function that will score each generated string by comparing the randomly generated string to the goal.
def score(goal_str, compare_str):
    number_of_same_chars = 0
    # Loop though and compare eachother base on goalStr length
    for i in range(len(goal_str)):
        if goal_str[i] == compare_str[i]:
            number_of_same_chars = number_of_same_chars + 1

    return number_of_same_chars


# 3, A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
def mainFunction():
    start_time = time.time()
    best_score = 0
    best_str = ""
    goal_str = "methinks it is like aweasel"
    for i in range(1000000):
        compare_str = attempt(27)
        compared_result = score(goal_str, compare_str)
        # print("Random str result >>> ", "'" + str(compare_str) + "'")
        # print("Compare result >>> ", compared_result)
        if best_score < compared_result:
            best_score = compared_result
            best_str = compare_str


    print("Best score >>> ", best_score)
    print("Best string >>> ", "'" + best_str + "'")
    end_time = time.time()
    print("Run time >>> ", str(end_time - start_time) + "s")

mainFunction()
