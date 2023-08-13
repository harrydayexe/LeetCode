import unittest
from v2 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(sorted(expected), sorted(Solution.threeSum(nums)))

    def test_case_2(self):
        nums = [0, 1, 1]
        expected = []
        self.assertEqual(sorted(expected), sorted(Solution.threeSum(nums)))

    def test_case_3(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertEqual(sorted(expected), sorted(Solution.threeSum(nums)))


if __name__ == '__main__':
    unittest.main()
