# write a boolean function that will take two strings and return whether they are anagrams.

# Solution One - Checking Off
# We need to note that each charactors in str1 will cause an intraction though up to n charactors in str_arr_two.
# Each of the 𝑛 positions in the list will be visited once to match a character from str1.
# The number of visits will be sum of the integers from 1 to n. Such as
# n(n+1)/2 = n^2/2 + n/2
# As 𝑛 gets large, the 𝑛^2 term will dominate the 𝑛 term and the 1 can be ignored.
# Therefore, this solution is 𝑂(𝑛^2).

def anagram_solution_one(str1, str2):
    # Str into array
    str_arr_two = list(str2)

    position1 = 0
    still_loop = True

    while position1 < len(str1) and still_loop:
        position2 = 0
        found = False
        while position2 < len(str_arr_two) and not found:
            if str1[position1] == str_arr_two[position2]:
                found = True
            else:
                position2 = position2 + 1

        if found:
            str_arr_two[position2] = None
        else:
            still_loop = False

        position1 = position1 + 1

    return still_loop




re1 = anagram_solution_one("okk", "0ok")
# print(re1)

# Solution Two - Sort and Compare
# We need to note that sort() is is typically either 𝑂(n^2) or 𝑂(n log n)
#
def anagram_solution_two(str1, str2):
    arr1 = list(str1)
    arr2 = list(str2)

    arr1.sort()
    arr2.sort()

    position = 0
    matches = True

    while position < len(str1) and matches:
        if arr1[position] == arr2[position]:
            position = position + 1
        else:
            matches = False

    return matches


re2 = anagram_solution_two("abeds", "aesbd")
# print(re2)


# Solution Three - Brute Force
# Create as many possible letters from the input str.
# For example, if the is a 20 char string, there will be 20 initial letter patterns.
# And the second char will be 19 char patterns.
# 20!
# Due to there reasons, it is not a good solution.


# Solution Four - Count and Compare

def anagram_solution_four(str1, str2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(str1)):
        # ord(a) = 97, ord(str1[0]) = ord(a), ord(str1[i]) - ord('a') = 0
        # +1 at the sub integer index
        position = ord(str1[i]) - ord('a')
        c1[position] = c1[position] + 1

    for i in range(len(str2)):
        # ord(a) = 97, ord(str1[0]) = ord(a), ord(str1[i]) - ord('a') = 0
        # +1 at the sub integer index
        position = ord(str2[i]) - ord('a')
        c2[position] = c2[position] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            print("HIT >> ", c1[j], c2[j])
            still_ok = False

    return still_ok



re4 = anagram_solution_four("apple", "pleap")
print(re4)
