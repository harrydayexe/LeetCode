import unittest
from v3 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(Solution.containsDuplicate(nums=nums))

    def test_case_2(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(Solution.containsDuplicate(nums=nums))

    def test_case_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(Solution.containsDuplicate(nums=nums))


if __name__ == '__main__':
    unittest.main()
