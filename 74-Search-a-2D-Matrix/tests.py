import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_case_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_case_3(self):
        matrix = [[1]]
        target = 0
        self.assertFalse(self.solution.searchMatrix(matrix, target))

    def test_case_4(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_case_5(self):
        matrix = [[1, 1]]
        target = 1
        self.assertTrue(self.solution.searchMatrix(matrix, target))

    def test_case_6(self):
        matrix = [[1, 3, 5]]
        target = 1
        self.assertTrue(self.solution.searchMatrix(matrix, target))

if __name__ == '__main__':
    unittest.main()
