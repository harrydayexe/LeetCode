public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visitedNodes = new HashSet<ListNode>();

        while (head != null) {
            if (visitedNodes.contains(head)) {
                return true;
            } else {
                visitedNodes.add(head);
            }
            head = head.next;
        }
        return false;
    }
}
