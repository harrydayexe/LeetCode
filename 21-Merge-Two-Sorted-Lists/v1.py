from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None and list2 is None:

        output = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                # list2 is not None
                output = self.appendListNode(output, list2)
                list2 = None
            elif list2 is None:
                # list1 is not None
                output = self.appendListNode(output, list1)
                list1 = None
            else:
                if list1.val <= list2.val:
                    next_val = list1.val
                    list1 = list1.next
                else:
                    next_val = list2.val
                    list2 = list2.next
                output = self.appendListNode(output, ListNode(next_val))

        return output

    def appendListNode(self, head: Optional[ListNode], node: Optional[ListNode]):
        if node is None:
            return head
        elif head is None:
            return node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = node
            return head