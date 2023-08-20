import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(expected, self.solution.generateParenthesis(3))

    def test_case_2(self):
        expected = ["()"]
        self.assertEqual(expected, self.solution.generateParenthesis(1))


if __name__ == '__main__':
    unittest.main()
