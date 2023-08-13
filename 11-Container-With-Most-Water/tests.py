import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(expected, Solution.maxArea(height))

    def test_case_2(self):
        height = [1, 1]
        expected = 1
        self.assertEqual(expected, Solution.maxArea(height))

    def test_case_3(self):
        height = [1, 2, 4, 3]
        expected = 4
        self.assertEqual(expected, Solution.maxArea(height))


if __name__ == '__main__':
    unittest.main()
