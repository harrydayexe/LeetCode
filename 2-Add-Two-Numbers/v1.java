class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        StringBuilder number1Builder = new StringBuilder();
        StringBuilder number2Builder = new StringBuilder();

        while (l1 != null) {
            number1Builder.append(l1.val);
            l1 = l1.next;
        }

        while (l2 != null) {
            number2Builder.append(l2.val);
            l2 = l2.next;
        }

        int number1 = Integer.parseInt(number1Builder.reverse().toString());
        int number2 = Integer.parseInt(number2Builder.reverse().toString());
        String totalString = Integer.toString(number1 + number2);

        ListNode output = new ListNode((int)totalString.charAt(0)-'0');
        for (int i=1; i < totalString.length(); i++) {
            output = new ListNode((int)totalString.charAt(i)-'0', output);
        }

        return output;
    }
}
