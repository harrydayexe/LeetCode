lass Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        Node temp = head;
        Node copy = new Node(head.val);
        Node copyHead = copy;

        HashMap memoryMap = new HashMap<Node, Node>();
        memoryMap.put(head, copy);

        while (temp.next != null) {
            copy.next = new Node(temp.next.val);
            memoryMap.put(temp.next, copy.next);
            temp = temp.next;
            copy = copy.next;
        }

        temp = head;
        copy = copyHead;
        while (temp != null) {
            if (temp.random != null) {
                copy.random = (Node) memoryMap.get(temp.random);
            }

            temp = temp.next;
            copy = copy.next;
        }

        return copyHead;
    }
}
