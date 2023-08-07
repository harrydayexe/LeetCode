import unittest
from v2 import Solution as Solution


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(Solution.isAnagram(s=s, t=t))

    def test_case_2(self):
        s = "rat"
        t = "cat"
        self.assertFalse(Solution.isAnagram(s=s, t=t))


if __name__ == '__main__':
    unittest.main()
