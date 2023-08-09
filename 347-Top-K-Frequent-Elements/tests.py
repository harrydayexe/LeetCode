import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        expected = [1, 2]
        actual = Solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        expected = [1]
        actual = Solution.topKFrequent([1], 1)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
