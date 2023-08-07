import unittest
from v2 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        answer = Solution.twoSum(nums, target)

        self.assertEqual(answer, [0, 1])

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        answer = Solution.twoSum(nums, target)

        self.assertEqual(answer, [1, 2])

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        answer = Solution.twoSum(nums, target)

        self.assertEqual(answer, [0, 1])


if __name__ == '__main__':
    unittest.main()
