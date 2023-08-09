import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        actual = Solution.productExceptSelf(nums)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        actual = Solution.productExceptSelf(nums)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
