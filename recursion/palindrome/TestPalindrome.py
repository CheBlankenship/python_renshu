# python -m unittest TestPalindrome

import unittest
from unittest import TestCase
from palindrome1 import palindrome_checker




class TestPalindrome(unittest.TestCase):

        # Success Case 1
    def test_palindrome_success_case(self):
        input_string = "kayak"
        expected_output = True
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # Success Case 2
    def test_palindrome_success_two(self):
        input_string = "aibohphobia"
        expected_output = True
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # Success Case 3
    def test_palindrome_success_three(self):
        input_string = "Live not on evil"
        expected_output = True
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # Success Case 4
    def test_palindrome_success_four(self):
        input_string = "Reviled did I live, said I, as evil I did deliver"
        expected_output = True
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # Success Case 5
    def test_palindrome_success_five(self):
        input_string = "Go hang a salami; I’m a lasagna hog."
        expected_output = True
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # # False Case 6
    def test_palindrome_success_six(self):
        input_string = "Able was I ere I saw Elba"
        expected_output = True
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # # False Case 2
    def test_palindrome_false_two(self):
        input_string = "Kanakanak – a town in Alaska"
        expected_output = False
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)

        # # False Case 3
    def test_palindrome_false_three(self):
        input_string = "Wassamassaw – a town in South Dakota"
        expected_output = False
        return_value = palindrome_checker(input_string)
        self.assertEqual(expected_output, return_value)




    if __name__ == "__main__":
        unittest.main()
