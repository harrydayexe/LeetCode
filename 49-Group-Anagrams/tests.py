import unittest
from v1 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        given = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual = Solution.groupAnagrams(given)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        given = [""]
        expected = [[""]]
        actual = Solution.groupAnagrams(given)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        given = ["a"]
        expected = [["a"]]
        actual = Solution.groupAnagrams(given)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        given = ["", ""]
        expected = [["", ""]]
        actual = Solution.groupAnagrams(given)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
