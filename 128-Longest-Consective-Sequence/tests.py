import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
        actual = Solution.longestConsecutive(nums)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
        actual = Solution.longestConsecutive(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
