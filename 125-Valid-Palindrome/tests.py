import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(Solution.isPalindrome(s))

    def test_case_2(self):
        s = "race a car"
        self.assertFalse(Solution.isPalindrome(s))

    def test_case_3(self):
        s = " "
        self.assertTrue(Solution.isPalindrome(s))


if __name__ == '__main__':
    unittest.main()
