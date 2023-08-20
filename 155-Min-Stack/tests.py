import unittest
from v1 import MinStack as MinStack


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(-3, stack.getMin())
        stack.pop()
        self.assertEqual(0, stack.top())
        self.assertEqual(-2, stack.getMin())


if __name__ == '__main__':
    unittest.main()
