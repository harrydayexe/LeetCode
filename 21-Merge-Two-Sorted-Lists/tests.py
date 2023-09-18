import unittest
from v1 import *


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        l1 = ListNode(1, ListNode(2, ListNode(4)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        self.assertTrue(self.equal_lists(expected, self.solution.mergeTwoLists(l1, l2)))

    def test_case_2(self):
        l1 = None
        l2 = None
        expected = None
        self.assertTrue(self.equal_lists(expected, self.solution.mergeTwoLists(l1, l2)))

    def test_case_3(self):
        l1 = None
        l2 = ListNode(0)
        expected = ListNode(0)
        self.assertTrue(self.equal_lists(expected, self.solution.mergeTwoLists(l1, l2)))

    def equal_lists(self, list1, list2):
        while list1 is not None and list2 is not None:
            if list1.val != list2.val:
                return False
            else:
                list1 = list1.next
                list2 = list2.next

        if list1 != list2:
            return False
        else:
            return True


if __name__ == '__main__':
    unittest.main()
