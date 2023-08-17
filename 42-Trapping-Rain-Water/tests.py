import unittest
from v2 import Solution as Solution

solution = Solution()

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        self.assertEqual(expected, solution.trap(height))

    def test_case_2(self):
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        self.assertEqual(expected, solution.trap(height))


if __name__ == '__main__':
    unittest.main()
