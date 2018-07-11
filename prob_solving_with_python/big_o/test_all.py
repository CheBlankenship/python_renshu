from unittest import TestCase
from nose.tools import *
from first_script import solution


# Define unit test module
class SolutionTest(TestCase):

    def setUp(self):
        print('before test')

    def tearDown(self):
        print('after test')

    # Success cases
    def test_one(self, sol_one):
        eq_(sol_one(2,2), 4)
        eq_(sol_one(4,4), 8)

    # Negative case
    # def test_two(self, sol_two):
    #     eq_(sol_two("hola", "hola"), 4)
    #     print("All tast cases passed")



# Call class SolutionTest as t
# t = SolutionTest()
# Access test module
# t.test_one(solution)
# t.test_two(solution)
