import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertEqual(expected, self.solution.dailyTemperatures(temperatures))

    def test_case_2(self):
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]
        self.assertEqual(expected, self.solution.dailyTemperatures(temperatures))

    def test_case_3(self):
        temperatures = [30, 60, 90]
        expected = [1, 1, 0]
        self.assertEqual(expected, self.solution.dailyTemperatures(temperatures))


if __name__ == '__main__':
    unittest.main()
