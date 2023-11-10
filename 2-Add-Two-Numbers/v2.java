class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        int total = 0;
        
        while (l1 != null || l2 != null || total > 0) {
            if (l1 != null) {
                total += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                total += l2.val;
                l2 = l2.next;
            }

            cur.next = new ListNode(total % 10);
            cur = cur.next;
            total = total / 10;
        }

        return dummy.next;
    }
}
