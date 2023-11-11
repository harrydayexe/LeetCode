class Node {
    int key;
    int val;
    Node prev;
    Node next;

    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    HashMap<Integer, Node> cache;
    int capacity;
    Node left;
    Node right;

    public LRUCache(int capacity) {
        this.cache = new HashMap<Integer, Node>(capacity+1);
        this.capacity = capacity;
        this.left = new Node(0, 0); this.right = new Node(0, 0);
        this.left.next = this.right; this.right.prev = this.left;
    }

    private void insert(Node node) {
        Node prev = right.prev; Node next = right;
        prev.next = node; next.prev = node;
        node.prev = prev; node.next = next;
    }

    private void remove(Node node) {
        Node prev = node.prev; Node next = node.next;
        prev.next = next; next.prev = prev;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            remove(cache.get(key));
            insert(cache.get(key));
            return cache.get(key).val;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            remove(cache.get(key));
        }

        cache.put(key, new Node(key, value));
        insert(cache.get(key));

        if (cache.size() > capacity) {
            Node lru = left.next;
            remove(lru);
            cache.remove(lru);
        }
    }
}
