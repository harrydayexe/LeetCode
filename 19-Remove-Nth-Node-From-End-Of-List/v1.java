class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 1;
        ListNode nextNode = head;
        while (nextNode.next != null) {
            nextNode = nextNode.next;
            count += 1;
        }

        System.out.println(count);

        if (count == 1) {
            return null;
        } 
        if (count == 2) {
            if (n == 1) {
                head.next = null;
                return head;
            } else {
                return head.next;
            }
        }

        nextNode = head;
        if (count-n == 0) {
            return head.next;
        }

        for (int i=1; i <count-n; i++) {
            nextNode = nextNode.next;
        }

        nextNode.next = nextNode.next.next;
        return head;
    }
}
