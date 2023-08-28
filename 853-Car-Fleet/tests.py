import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        self.assertEqual(3, self.solution.carFleet(target, position, speed))

    def test_case_2(self):
        target = 10
        position = [3]
        speed = [3]
        self.assertEqual(1, self.solution.carFleet(target, position, speed))

    def test_case_3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        self.assertEqual(1, self.solution.carFleet(target, position, speed))

    def test_case_4(self):
        target = 10
        position = [0, 4, 2]
        speed = [2, 1, 3]
        self.assertEqual(1, self.solution.carFleet(target, position, speed))


if __name__ == '__main__':
    unittest.main()
