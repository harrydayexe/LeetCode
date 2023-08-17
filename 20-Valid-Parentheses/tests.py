import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        s = "()"
        self.assertTrue(solution.isValid(s))

    def test_case_2(self):
        solution = Solution()
        s = "()[]{}"
        self.assertTrue(solution.isValid(s))

    def test_case_3(self):
        solution = Solution()
        s = "(]"
        self.assertFalse(solution.isValid(s))


if __name__ == '__main__':
    unittest.main()
