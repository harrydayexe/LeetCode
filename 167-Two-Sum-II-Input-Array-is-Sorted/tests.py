import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        self.assertEqual(expected, Solution.twoSum(numbers, target))

    def test_case_2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        self.assertEqual(expected, Solution.twoSum(numbers, target))

    def test_case_3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        self.assertEqual(expected, Solution.twoSum(numbers, target))


if __name__ == '__main__':
    unittest.main()
