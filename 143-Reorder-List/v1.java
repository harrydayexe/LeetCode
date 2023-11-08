class Solution {
    public void reorderList(ListNode head) {
        if (head.next == null) {
            return;
        } 
        if (head.next.next == null) {
            return;
        }

        ListNode lastButOne = head;

        while (lastButOne.next.next != null) {
            lastButOne = lastButOne.next;
        }

        ListNode last = lastButOne.next;
        lastButOne.next = null;

        reorderList(head.next);
        last.next = head.next;
        head.next = last;

        return;
    }
}
