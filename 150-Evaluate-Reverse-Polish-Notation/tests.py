import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(9, self.solution.evalRPN(tokens))

    def test_case_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(6, self.solution.evalRPN(tokens))

    def test_case_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(22, self.solution.evalRPN(tokens))


if __name__ == '__main__':
    unittest.main()
