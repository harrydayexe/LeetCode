from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveReverseList(head, None)

    def recursiveReverseList(self, head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            # Base case
            return prev
        else:
            # Step case
            return self.recursiveReverseList(head.next, ListNode(head.val, prev))

