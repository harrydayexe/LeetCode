import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(4, self.solution.search(nums, target))

    def test_case_2(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        self.assertEqual(-1, self.solution.search(nums, target))


if __name__ == '__main__':
    unittest.main()
